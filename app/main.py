from fastapi import FastAPI, HTTPException, Depends, Security, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field
from app.processor import TextProcessor
import os

# Initialize FastAPI app
app = FastAPI(
    title="ML Preprocessing API",
    description="Secure REST API for text normalization.",
    version="1.0.0"
)

# API Key Header configuration
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# In a real app, this should be loaded from an environment variable, not hardcoded
REAL_SECRET_KEY = "super-segreto-123"

async def get_api_key(api_key_header: str = Security(api_key_header)):
    
    # Dependency function that checks if the key is valid.
    
    if api_key_header == REAL_SECRET_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials (Missing API Key or wrong key)"
        )

# Request model
class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The text to process")
    remove_digits: bool = Field(False, description="If True, removes numbers")

# Response model
class TextResponse(BaseModel):
    original_text: str
    processed_text: str
    stats: dict
    status: str

# Endpoint to process text
@app.post("/process", response_model=TextResponse, dependencies=[Depends(get_api_key)])
def process_text(request: TextRequest):
    try:
        processor = TextProcessor(remove_digits=request.remove_digits)
        clean_result = processor.clean_text(request.text)
        stats = processor.analyze_stats(clean_result)
        
        return {
            "original_text": request.text,
            "processed_text": clean_result,
            "stats": stats,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")  # Health check endpoint
def health_check():
    return {"status": "ok"}
