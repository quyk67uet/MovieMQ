<template>
    <div class="chat-container">
      <div class="chat-box">
        <div class="chat-header">
          <h2>MovieBot</h2>
        </div>
        <div class="chat-messages">
          <div v-for="(message, index) in messages" :key="index" :class="{'chat-message': true, 'user-message': message.startsWith('You: '), 'bot-message': message.startsWith('Bot: ')}">
            {{ message }}
          </div>
        </div>
        <div class="chat-footer">
          <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
          <button @click="sendMessage">Send</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'ChatBox',
    data() {
      return {
        newMessage: '',
        messages: []
      };
    },
    methods: {
      async sendMessage() {
        if (this.newMessage.trim() === '') return;
  
        const query = this.newMessage;
        this.newMessage = '';
        this.messages.push(`You: ${query}`);
  
        try {
          const response = await axios.post(`http://127.0.0.1:8000/chat_with_knowledge_base?query=${encodeURIComponent(query)}`);
          const responseText = response.data.response;
          this.messages.push(`Bot: ${responseText}`);
        } catch (error) {
          console.error('Error:', error);
          this.messages.push('Bot: Sorry, I didn\'t get that.');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-image: url('@/assets/back3.jpg'); 
    background-size: cover;
    background-position: center;
  }
  
  .chat-box {
    border: 1px solid #ccc;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 600px;
    height: 80%;
    background-color: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .chat-header {
    background-color: #e1d24a;
    color: white;
    padding: 10px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .chat-messages {
    padding: 10px;
    flex: 1;
    overflow-y: auto;
    margin-bottom: 10px;
  }
  
  .chat-message {
    margin-bottom: 10px;
    word-wrap: break-word;
    padding: 10px;
    border-radius: 5px;
    max-width: 80%;
  }
  
  .user-message {
    background-color: #dcf8c6;
    align-self: flex-end;
  }
  
  .bot-message {
    background-color: #f1f0f0;
    align-self: flex-start;
  }
  
  .chat-footer {
    padding: 10px;
    border-top: 1px solid #ddd;
    display: flex;
  }
  
  input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-right: 10px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #e1d24a;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #bcb535;
  }
  </style>