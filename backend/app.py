#!/usr/bin/env python3
"""
Backend API for new- project

FastAPI backend providing REST API endpoints for the utility functions.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from utils import greet, format_version, slugify, truncate

app = FastAPI(
    title="new- API",
    description="REST API for essential Python utilities",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class GreetRequest(BaseModel):
    name: str

class FormatVersionRequest(BaseModel):
    version: str

class SlugifyRequest(BaseModel):
    text: str

class TruncateRequest(BaseModel):
    text: str
    max_length: int = 50
    suffix: str = "..."

# API Endpoints
@app.get("/")
async def root():
    """Root endpoint with API info."""
    return {
        "message": "new- API - Essential Python Utilities",
        "version": "1.0.0",
        "endpoints": [
            "/greet",
            "/format-version", 
            "/slugify",
            "/truncate",
            "/health"
        ]
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "new- API"}

@app.post("/greet")
async def greet_endpoint(request: GreetRequest):
    """Generate greeting message."""
    try:
        result = greet(request.name)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/format-version")
async def format_version_endpoint(request: FormatVersionRequest):
    """Format version string."""
    try:
        result = format_version(request.version)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/slugify")
async def slugify_endpoint(request: SlugifyRequest):
    """Convert text to URL-friendly slug."""
    try:
        result = slugify(request.text)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/truncate")
async def truncate_endpoint(request: TruncateRequest):
    """Truncate text to specified length."""
    try:
        result = truncate(request.text, request.max_length, request.suffix)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
