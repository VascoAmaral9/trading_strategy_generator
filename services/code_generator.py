"""Code generation service using AI clients."""
from services.ai_client import AIClientManager
from prompts.templates import (
    get_trade_code_prompt,
    get_docstring_prompt,
    build_messages
)


class CodeGenerator:
    """Handles code generation using AI models."""
    
    def __init__(self):
        self.client_manager = AIClientManager()
    
    def generate_trade_code(self, model: str, currency: str, wallet_balance: float) -> str:
        """Generate trading strategy code."""
        client = self.client_manager.get_client(model)
        prompt = get_trade_code_prompt(currency, wallet_balance)
        messages = build_messages(prompt)
        
        reasoning_effort = "high" if self.client_manager.should_use_reasoning(model) else None
        
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            reasoning_effort=reasoning_effort
        )
        
        return response.choices[0].message.content
    
    def add_comments(self, model: str, python_code: str) -> str:
        """Add docstrings and comments to existing code."""
        client = self.client_manager.get_client(model)
        prompt = get_docstring_prompt(python_code)
        messages = build_messages(prompt)
        
        reasoning_effort = "high" if self.client_manager.should_use_reasoning(model) else None
        
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            reasoning_effort=reasoning_effort
        )
        
        return response.choices[0].message.content
