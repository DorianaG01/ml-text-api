from fastapi import FastAPI, HTTPException, Depends, Security, status
from fastapi.security import APIKeyHeader  
from pydantic import BaseModel, Field
from app.processor import TextProcessor
import os

# Inizializzazione dell'app FastAPI
app = FastAPI(
    title="ML Preprocessing API",
    description="API REST sicura per la normalizzazione del testo.",
    version="1.0.0"
)

# Configurazione API Key Header
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False) 

# Questa è la vera chiave segreta, in un'app reale andrebbe caricata da una variabile d'ambiente e non scritta nel codice
REAL_SECRET_KEY = "super-segreto-123"

async def get_api_key(api_key_header: str = Security(api_key_header)):
   
    #Funzione di dipendenza che controlla se la chiave è valida.
   
    if api_key_header == REAL_SECRET_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Credenziali non valide (Manca API Key o è errata)"
        )

# Modello di richiesta
class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Il testo da processare") 
    remove_digits: bool = Field(False, description="Se True, rimuove i numeri")

# Modello di risposta
class TextResponse(BaseModel):
    original_text: str
    processed_text: str
    stats: dict
    status: str

# Endpoint per processare il testo
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

@app.get("/health")  # Endpoint di health check
def health_check():
    return {"status": "ok"}