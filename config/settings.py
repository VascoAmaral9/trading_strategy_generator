"""Configuration settings for the trading strategy generator."""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# API URLs
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GROQ_URL = "https://api.groq.com/openai/v1"
OLLAMA_URL = "http://localhost:11434/v1"

# Available models and currencies
MODELS = ["gpt-5", "gemini-2.5-pro", "gpt-oss:20b", "openai/gpt-oss-120b"]
CURRENCIES = ["BTC", "ETH", "SOL", "ADA"]

# Default values
DEFAULT_CURRENCY = "BTC"
DEFAULT_WALLET_BALANCE = 1000
DEFAULT_MODEL = "gpt-5"
