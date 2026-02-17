# Backend API

FastAPI backend for the new- project providing REST API endpoints.

## 🚀 Features

- **RESTful API** for all utility functions
- **CORS enabled** for frontend integration
- **Pydantic models** for request validation
- **Error handling** with proper HTTP status codes
- **Health check** endpoint
- **Auto-generated docs** at `/docs`

## 📦 Installation

```bash
cd backend
pip install -r requirements.txt
```

## 🏃‍♂️ Running

```bash
# Development
python app.py

# Production
uvicorn app:app --host 0.0.0.0 --port 8000
```

## 📚 API Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `POST /greet` - Generate greeting
- `POST /format-version` - Format version
- `POST /slugify` - Create slug
- `POST /truncate` - Truncate text

## 📖 Documentation

Visit `http://localhost:8000/docs` for interactive API documentation.
