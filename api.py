# MOCK DE API PARA AGENTE INTELIGENTE DE CGP CODE
# Plataforma: FastAPI (Python)
# Objetivo: Demostrar capacidad en APIs, Automatización y uso de Modelos de Lenguaje (IA)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

# 1. Definición del modelo de datos de entrada/salida (Pydantic para validación)
class MessageRequest(BaseModel):
    """Modelo de Pydantic para la solicitud del cliente."""
    client_id: str
    message: str

class ResponseAnalysis(BaseModel):
    """Modelo de Pydantic para la respuesta de la API."""
    response_type: str
    context_summary: str
    suggested_action: str
    confidence_score: float

# 2. Inicialización de la API
app = FastAPI(
    title="CGP Code AI Agent Service Mock",
    description="Motor de análisis de lenguaje natural (NLP) para automatización de servicios de software e IA.",
    version="1.0.0"
)

# 3. Función de Lógica (Simulación de IA/NLP)
def analyze_message_with_ai(message: str) -> Dict:
    """Simula el procesamiento avanzado de un mensaje, como si usáramos la Gemini API."""
    
    message_lower = message.lower()
    
    # Simulación de Clasificación basada en la nueva visión de CGP Code
    if "bug" in message_lower or "error" in message_lower or "vulnerabilidad" in message_lower:
        summary = "El cliente reporta una incidencia de seguridad o un bug en el código."
        action = "Crear ticket en el Help Desk y adjuntar logs."
        response_type = "Incidencia Software/Seguridad"
        score = 0.98
    elif "prototipo" in message_lower or "requisitos" in message_lower or "mvp" in message_lower:
        summary = "El cliente solicita una nueva funcionalidad, prototipo o análisis de requisitos."
        action = "Redirigir al equipo de Ingeniería de Requisitos y modelado UML."
        response_type = "Análisis de Requisitos"
        score = 0.92
    elif "automatizar" in message_lower or "workspace" in message_lower or "whatsapp" in message_lower:
        summary = "El cliente solicita información sobre automatización o integración de APIs (CRM/Workspace)."
        action = "Enviar documentación sobre integración de la Gemini API y Twilio/Meta Graph API."
        response_type = "Automatización/API"
        score = 0.95
    else:
        summary = "Consulta general. Requiere escalamiento."
        action = "Responder con saludo contextualizado y transferir a soporte."
        response_type = "Consulta General"
        score = 0.70

    return {
        "response_type": response_type,
        "context_summary": summary,
        "suggested_action": action,
        "confidence_score": score
    }

# 4. Endpoint Principal de la API (POST)
@app.post("/analyze-agent-message", response_model=ResponseAnalysis, status_code=200)
async def analyze_message(request: MessageRequest):
    """
    Analiza un mensaje entrante de un cliente y clasifica la intención para automatizar la acción.
    """
    try:
        analysis_result = analyze_message_with_ai(request.message)
        return ResponseAnalysis(**analysis_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del sistema: {e}")