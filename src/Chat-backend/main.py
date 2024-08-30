from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from sentence_transformers import SentenceTransformer

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
GEMINI_KEY = os.getenv("GEMINI_KEY")
DB_COLLECTION = os.getenv("DB_COLLECTION")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# Initialize FastAPI app
app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize MongoDB Atlas client
mongo_client = MongoClient(MONGODB_URI)
db = mongo_client[DB_NAME]  # Use the database name from .env
collection = db[DB_COLLECTION]  # Use the collection name from .env

genai.configure(api_key=GEMINI_KEY)
llm = genai.GenerativeModel('gemini-1.5-flash')
# Initialize SentenceTransformer for embedding generation
embedding_model = SentenceTransformer(EMBEDDING_MODEL)

def get_embedding(text: str) -> list[float]:
    """Generate embedding for a given text using the SentenceTransformer model."""
    if not text.strip():
        print("Attempted to get embedding for empty text.")
        return []

    embedding = embedding_model.encode(text)
    return embedding.tolist()

def vector_search(user_query: str, collection):
    """
    Perform a vector search in the MongoDB collection based on the user query.
    Args:
        user_query (str): The user's query string.
        collection (MongoCollection): The MongoDB collection to search.
    Returns:
        list: A list of matching documents.
    """
    # Generate embedding for the user query
    query_embedding = get_embedding(user_query)
    
    if not query_embedding:
        return {"error": "Invalid query or embedding generation failed."}
    
    # Define the vector search pipeline
    vector_search_stage = {
        "$vectorSearch": {
            "index": "vector_index",
            "queryVector": query_embedding,
            "path": "embedding",
            "numCandidates": 150,  # Number of candidate matches to consider
            "limit": 4  # Return top 4 matches
        }
    }
    
    unset_stage = {
        "$unset": "embedding"  # Exclude the 'embedding' field from the results
    }
    
    project_stage = {
        "$project": {
            "_id": 0,  # Exclude the _id field
            "fullplot": 1,  # Include the plot field
            "title": 1,  # Include the title field
            "genres": 1,  # Include the genres field
            "score": {
                "$meta": "vectorSearchScore"  # Include the search score
            }
        }
    }
    
    pipeline = [vector_search_stage, unset_stage, project_stage]
    
    # Execute the search
    results = collection.aggregate(pipeline)
    return list(results)

def get_search_result(query, collection):

    get_knowledge = vector_search(query, collection)

    search_result = ""
    for result in get_knowledge:
        search_result += f"Title: {result.get('title', 'N/A')}, Plot: {result.get('fullplot', 'N/A')}\n"

    return search_result

def generate_response(query, collection):
    context = get_search_result(query, collection)
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = llm.generate_content(prompt)
    return response.text

@app.post("/chat_with_knowledge_base")
def chat_with_knowledge_base(query: str = Query(...)):
    """
    Endpoint to chat with the knowledge base using a vector search and language model.
    """
    try:

        # Use the LLM model to generate an answer based on the retrieved context
        llm_response = generate_response(query, collection)
        return JSONResponse(content={"response": llm_response}, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
