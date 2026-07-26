# Elevara Technology Stack (v1.0)

## Overview

This document defines the official technology stack for Elevara. It serves as the single source of truth for all engineering decisions and ensures consistency throughout the project lifecycle.

---

## Backend

| Component | Technology |
|----------|------------|
| Framework | FastAPI |
| Language | Python 3.14 |
| ORM | SQLAlchemy 2.x |
| Database Migration | Alembic |
| Validation | Pydantic v2 |
| ASGI Server | Uvicorn |

---

## Frontend

| Component | Technology |
|----------|------------|
| Framework | Next.js |
| Language | TypeScript |
| UI Library | React |
| Styling | Tailwind CSS |
| Components | shadcn/ui |

---

## Database

| Component | Technology |
|----------|------------|
| Primary Database | PostgreSQL |
| Cache | Redis |

---

## Artificial Intelligence

| Component | Technology |
|----------|------------|
| AI Gateway | Custom Provider-Agnostic Layer |
| Primary Providers | OpenAI, Google Gemini |
| Future Providers | Anthropic Claude, Azure OpenAI |

---

## Authentication

| Component | Technology |
|----------|------------|
| Authentication | JWT |
| Session Management | Refresh Tokens |
| Future Login Options | Google OAuth, Microsoft OAuth |

---

## Background Processing

| Component | Technology |
|----------|------------|
| Task Queue | Celery *(subject to review)* |

---

## DevOps

| Component | Technology |
|----------|------------|
| Containers | Docker |
| Container Orchestration | Docker Compose |
| CI/CD | GitHub Actions |

---

## Testing

| Component | Technology |
|----------|------------|
| Backend Testing | Pytest |
| Frontend Testing | Playwright |

---

## Version Control

| Component | Technology |
|----------|------------|
| Repository | GitHub |
| Branch Strategy | Git Flow (Main + Feature Branches) |

---

## API Documentation

| Component | Technology |
|----------|------------|
| API Docs | OpenAPI (Swagger UI) |

---

## Engineering Principles

- Build for scalability.
- Keep the business logic independent of frameworks.
- Prefer modular and maintainable architecture.
- Write tests for all core functionality.
- Document important decisions.
- Use AI responsibly and transparently.

---

## Status

**Version:** 1.0

**Project:** Elevara

**Last Updated:** July 2026