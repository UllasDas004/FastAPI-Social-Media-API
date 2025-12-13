# FastAPI Social Media API

A robust, full-featured Social Media RESTful API built with Python, FastAPI, and PostgreSQL.

## 🚀 Features

- **User Authentication**: Secure JWT-based authentication (Login/Registration).
- **Post Management**: Full CRUD support for posts (Create, Read, Update, Delete).
- **User Management**: Efficient user profile handling.
- **Database ORM**: Uses SQLAlchemy for interaction with PostgreSQL.
- **Data Validation**: Strict schemas using Pydantic.
- **Interactive Documentation**: Automatic Swagger UI generation.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Validation**: Pydantic
- **Server**: Uvicorn

## ⚡ Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL installed and running

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/UllasDas004/FastAPI-Social-Media-API.git
    cd FastAPI-Social-Media-API
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Configuration**
    *Note: Currently, database credentials are configured in `app/database.py`. An update to use Environment Variables is planned.*
    
    Ensure your local PostgreSQL database is running and credentials match the configuration.

5.  **Run the Server**
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be live at `http://127.0.0.1:8000`.

## 📚 Documentation

FastAPI automatically generates interactive API documentation.
- **Swagger UI**: Visit `/docs` (e.g., `http://127.0.0.1:8000/docs`) to test endpoints interactively.
- **ReDoc**: Visit `/redoc` for alternative documentation.

## 📁 Project Structure

```
FastAPI/
├── app/
│   ├── routers/       # API Route handlers (auth, posts, users)
│   ├── database.py    # Database connection & session
│   ├── main.py        # Application entry point
│   ├── models.py      # SQLAlchemy Database Models
│   ├── schemas.py     # Pydantic Schemas for validation
│   └── utils.py       # Helper functions (hashing, etc.)
├── requirements.txt
└── README.md
```
