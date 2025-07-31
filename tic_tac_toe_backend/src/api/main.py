from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.openai_chat import router as openai_chat_router

openapi_tags = [
    {"name": "chat", "description": "Endpoints for OpenAI chatbot communication."}
]

app = FastAPI(
    title="Tic-Tac-Toe Backend API",
    description="API for Tic-Tac-Toe game, includes chat functionality via OpenAI.",
    version="1.0.0",
    openapi_tags=openapi_tags,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(openai_chat_router)

@app.get("/", tags=["health"])
def health_check():
    """
    Health check endpoint for the backend service.
    """
    return {"message": "Healthy"}
