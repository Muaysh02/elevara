# 🚀 Elevara

> **AI-powered career assistant platform that helps users build resumes, generate personalized cover letters, discover relevant job opportunities, and manage their career journey with trustworthy AI.**

---

## 📖 About

Elevara is a modern AI-powered career platform designed to simplify every stage of a user's professional journey.

Instead of relying on multiple disconnected tools, Elevara provides one intelligent platform for creating application documents, discovering opportunities, tracking job applications, and receiving AI-powered career guidance.

The project is built with scalability, security, and maintainability in mind using modern backend engineering practices.

---

## ✨ Features

### Current

- User Management
- Professional Database Design
- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Database Migrations
- Environment-based Configuration

### Planned

- AI Resume Builder
- AI Cover Letter Generator
- Smart Job Matching
- Job Application Tracker
- Career Dashboard
- Subscription Management
- Admin Dashboard
- Multi-AI Provider Support (OpenAI & Gemini)

---

## 🏗 Tech Stack

### Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic Settings

### AI

- OpenAI
- Google Gemini

### Development

- Python 3
- Git
- Docker (Planned)

---

## 📂 Project Structure

```text
apps/backend
│
├── alembic/
├── app/
│   ├── core/
│   ├── db/
│   ├── models/
│   └── main.py
│
├── requirements.txt
└── alembic.ini
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/Muaysh02/elevara.git
```

```bash
cd elevara/apps/backend
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Environment Variables

Create a `.env` file.

Example:

```env
APP_NAME=Elevara API
APP_VERSION=1.0.0

DATABASE_URL=postgresql+psycopg://<username>:<password>@localhost:5432/elevara

JWT_SECRET_KEY=<your-secret>

REDIS_URL=redis://localhost:6379

OPENAI_API_KEY=

GEMINI_API_KEY=
```

---

### Database Migration

Generate migrations

```bash
alembic revision --autogenerate -m "message"
```

Apply migrations

```bash
alembic upgrade head
```

---

### Run Server

```bash
uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 🛣 Roadmap

- ✅ Backend Foundation
- ✅ PostgreSQL Database
- ✅ SQLAlchemy Models
- ✅ Alembic Migrations
- 🔄 Authentication & Authorization
- ⏳ Resume Builder
- ⏳ AI Cover Letter Generator
- ⏳ Job Matching
- ⏳ Career Dashboard
- ⏳ Subscription System
- ⏳ Admin Dashboard

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

Please open an issue first before submitting major changes.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Musa Abba**

GitHub:
https://github.com/Muaysh02

---

> Building the future of AI-powered career development.