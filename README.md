# 🎬 Movie Website

## Giới thiệu

Đây là một dự án website phim trực tuyến cho phép người dùng khám phá thông tin chi tiết về các bộ phim, diễn viên và các thông tin liên quan. Dự án được xây dựng bằng **Vue.js** (phiên bản 2) cho frontend và **FastAPI** cho backend. Ngoài ra, dự án còn tích hợp một chatbot tên **MovieBot** sử dụng mô hình **RAG (Retrieval-Augmented Generation)** để cung cấp các thông tin chi tiết và gợi ý phim cho người dùng.

![Movies](https://drive.google.com/uc?id=12VbFjSKQMSyhYeqwXjSkbblcK_BOSQSa)
![Movies](https://drive.google.com/uc?id=1rYVUhOcIY_FWYE4-qA0zs6-qlu2LEA9y)
![Movies](https://drive.google.com/uc?id=1eWpsF62Xa-PVWotH-KPAjEVK8rAMhv5O)
![Movies](https://drive.google.com/uc?id=1_RijSEPG4nJvz9X46WZ3K5uINnWQhA30)
![Movies](https://drive.google.com/uc?id=1VRdEGa6Ht6ODj2f4o0l6lIigVw0bh6GP)
![Movies](https://drive.google.com/uc?id=1TbDsmMkW53cZ3yi9pFsvxZjtmdR9nwK0)

## Tính năng chính

- **Tìm kiếm phim**: Người dùng có thể tìm kiếm thông tin chi tiết về các bộ phim, diễn viên và các thể loại phim.
- **Chatbot thông minh**: MovieBot hỗ trợ người dùng qua chức năng chat, cho phép người dùng thảo luận về các bộ phim, nhận gợi ý phim tương tự, và tìm hiểu thêm về các bộ phim cụ thể.
- **Giao diện người dùng thân thiện**: Sử dụng Vue.js để xây dựng giao diện người dùng hiện đại, dễ sử dụng, và tương thích với nhiều thiết bị.
- **Hiệu suất cao**: Backend sử dụng FastAPI giúp xử lý yêu cầu một cách nhanh chóng và hiệu quả.

## Công nghệ sử dụng

### Frontend
- **Vue.js 2**: Framework JavaScript mạnh mẽ cho việc xây dựng giao diện người dùng.
- **Vuetify**: Bộ công cụ giao diện người dùng dựa trên Vue.js, hỗ trợ thiết kế Material Design.
- **Axios**: Thư viện để thực hiện các yêu cầu HTTP từ frontend đến backend.

### Backend
- **FastAPI**: Framework web hiện đại và nhanh chóng để xây dựng các API với Python 3.7+.
- **Pydantic**: Thư viện để xác định và xác thực dữ liệu dựa trên Python type annotations.
- **RAG (Retrieval-Augmented Generation)**: Mô hình kết hợp giữa truy xuất thông tin và sinh văn bản, giúp MovieBot trả lời các câu hỏi của người dùng một cách chính xác và tự nhiên.

## Cài đặt

### Yêu cầu hệ thống

- **Node.js**: Phiên bản 12 trở lên
- **Python**: Phiên bản 3.7 trở lên

### Cài đặt frontend

1. **Cài đặt các dependencies**:
- Tạo 1 dự án MQ Movies
- Bật terminal chạy: vue create movie
- cd movie
- vue add vuetify
- npm install --save axios vue-axios
- npm install -s vue-carousel-3d
- npm install material-design-icons-iconfont -D
- Chạy frontend: npm run serve

## Cài đặt backend
- Cần phải tạo 1 database trên Mongodb (collection: movies)
- cd Chat-backend
- pip install -r requirements.txt
- uvicorn main:app --reload

  
