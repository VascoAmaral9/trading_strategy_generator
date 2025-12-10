"""AI client initialization and management."""
from openai import OpenAI
from config.settings import (
    OPENAI_API_KEY,
    GOOGLE_API_KEY,
    GROQ_API_KEY,
    GEMINI_URL,
    GROQ_URL,
    OLLAMA_URL
)


class AIClientManager:
    """Manages AI client instances for different providers."""
    
    def __init__(self):
        self.openai = OpenAI(api_key=OPENAI_API_KEY)
        self.gemini = OpenAI(api_key=GOOGLE_API_KEY, base_url=GEMINI_URL)
        self.groq = OpenAI(api_key=GROQ_API_KEY, base_url=GROQ_URL)
        self.ollama = OpenAI(api_key="ollama", base_url=OLLAMA_URL)
        
        self.clients = {
            "gpt-5": self.openai,
            "gemini-2.5-pro": self.gemini,
            "openai/gpt-oss-120b": self.groq,
            "gpt-oss:20b": self.ollama
        }
    
    def get_client(self, model: str):
        """Get the appropriate client for a given model."""
        return self.clients.get(model)
    
    def should_use_reasoning(self, model: str) -> bool:
        """Determine if reasoning effort should be used for a model."""
        return 'gpt' in model.lower()
