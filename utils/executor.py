"""Utilities for executing Python code safely."""
import io
import sys


def execute_code(code: str) -> str:
    """
    Execute Python code and capture output.
    
    Args:
        code: Python code string to execute
        
    Returns:
        String containing the captured output
    """
    # Remove markdown formatting if present
    code = code.replace('```python\n', '').replace('```', '')
    
    try:
        output = io.StringIO()
        sys.stdout = output
        exec(code)
    finally:
        sys.stdout = sys.__stdout__
    
    return output.getvalue()
