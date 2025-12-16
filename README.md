<div align="center">
  <img src="assets/banner.png" alt="FastAPI Social Media API Banner" width="100%" />

  # FastAPI Social Media API
  
  <p>
    <b>Robust • Scalable • Secure</b>
  </p>

  ![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql&logoColor=white)

  <br />
  
  A robust, full-featured **Social Media RESTful API** built with high-performance modern tools. <br />
  Designed for scalability, security, and developer experience.

  [**Explore Docs »**](#-documentation)
  <br />
  [Report Bug](https://github.com/UllasDas004/FastAPI-Social-Media-API/issues)
  ·
  [Request Feature](https://github.com/UllasDas004/FastAPI-Social-Media-API/issues)
</div>

---

## 🚀 Features

| Feature | Description |
| :--- | :--- |
| 🔐 **Authentication** | Secure **JWT-based** system with Login/Registration & Password Hashing. |
| 📝 **Post Management** | Complete CRUD operations (Create, Read, Update, Delete) for content. |
| 👍 **Voting System** | Real-time **Like/Vote** functionality for community engagement. |
| 👤 **User Profiles** | Efficient management of user data and relationships. |
| 🗄️ **ORM Integration** | Seamless database interaction using **SQLAlchemy** with PostgreSQL. |
| ✅ **Validation** | Strict data integrity checks using **Pydantic** schemas. |
| 📄 **Documentation** | Automatic, interactive API docs via **Swagger UI** & **ReDoc**. |
| 🏥 **Health Check** | Dedicated endpoint to monitor system status and uptime. |

## 🛠️ Tech Stack

<div align="center">

| Core | Database & ORM | DevOps & Tools |
| :---: | :---: | :---: |
| ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi) <br> ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white) <br> ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white) | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) <br> ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) |

</div>

- **Authentication**: JWT (JSON Web Tokens)
- **Validation**: Pydantic & Pydantic settings
- **Server**: Uvicorn (ASGI)

## ⚡ Quick Start

Get your local environment set up in minutes.

### Prerequisites
*   **Python 3.9+**
*   **PostgreSQL** (Running locally or via Docker)

### Installation

<details>
<summary><b>Click to show installation steps</b></summary>

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

4.  **Environment Configuration**
    
    Create a `.env` file in the root directory (based on `app/config.py`) and fill in your credentials:

    ```env
    DATABASE_HOSTNAME=localhost
    DATABASE_PORT=5432
    DATABASE_PASSWORD=your_password
    DATABASE_NAME=fastapi
    DATABASE_USERNAME=postgres
    SECRET_KEY=your_secret_key_here
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTE=30
    ```
</details>

### Run the Server

```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## 📚 Documentation

FastAPI provides beautiful, interactive documentation out of the box.

*   **Swagger UI**: Visit [`/docs`](http://127.0.0.1:8000/docs) to test endpoints.
*   **ReDoc**: Visit [`/redoc`](http://127.0.0.1:8000/redoc) for a documentation reading experience.

## 📁 Project Structure

```
FastAPI/
├── 📂 app/
│   ├── 📂 routers/       # 🛣️ API Routes (Auth, Posts, Users, Votes)
│   ├── 📜 config.py      # ⚙️ Environment Configuration
│   ├── 📜 database.py    # 🔌 Database Connection
│   ├── 📜 main.py        # 🚀 Entry Point
│   ├── 📜 models.py      # 🗄️ SQLAlchemy Models
│   ├── 📜 schemas.py     # ✅ Pydantic Schemas
│   └── 📜 utils.py       # 🛠️ Utilities (Hashing)
├── 📜 requirements.txt   # 📦 Dependencies
├── 📜 .env               # 🔒 Secrets (GitIgnored)
└── 📜 README.md
```

---

<div align="center">
  <p>Made with ❤️ by Ullas</p>
</div>
