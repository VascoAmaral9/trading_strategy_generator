"""UI event handlers for Gradio interface."""
from services.code_generator import CodeGenerator
from utils.executor import execute_code


class UIHandlers:
    """Handles UI events and interactions."""
    
    def __init__(self):
        self.code_generator = CodeGenerator()
    
    def on_generate_code(self, model: str, currency: str, wallet_balance: float) -> str:
        """Handle generate code button click."""
        return self.code_generator.generate_trade_code(model, currency, wallet_balance)
    
    def on_add_comments(self, model: str, python_code: str) -> str:
        """Handle add comments button click."""
        return self.code_generator.add_comments(model, python_code)
    
    def on_execute_code(self, code: str) -> str:
        """Handle execute code button click."""
        return execute_code(code)
