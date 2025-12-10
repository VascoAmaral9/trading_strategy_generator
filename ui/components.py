"""Gradio UI components for trading strategy generator."""
import gradio as gr
from config.settings import MODELS, CURRENCIES, DEFAULT_CURRENCY, DEFAULT_WALLET_BALANCE, DEFAULT_MODEL
from styles.styles import CSS
from ui.handlers import UIHandlers


def create_ui():
    """Create and configure the Gradio UI."""
    handlers = UIHandlers()
    
    with gr.Blocks(
        css=CSS,
        theme=gr.themes.Monochrome(),
        title="Crypto Trading Strategy Generator"
    ) as ui:
        gr.Markdown("""# CRYPTO TRADING STRATEGY GENERATOR 
                    
Generates trading Python code, which will recommend you whether to sell or buy a given crypto currency at its current price.

Based on the confidence level of the prediction it will recommend what amount should be placed from your available wallet balance""")
        
        # Control section
        with gr.Row(elem_classes=["controls"]):
            crypto_currency = gr.Dropdown(
                CURRENCIES,
                value=DEFAULT_CURRENCY,
                label="Crypto Currency"
            )
            wallet_balance = gr.Number(
                label="Wallet Balance (USDT)",
                value=DEFAULT_WALLET_BALANCE
            )
            model = gr.Dropdown(
                MODELS,
                value=DEFAULT_MODEL,
                label="AI Model"
            )
        
        # Generate button
        with gr.Row(equal_height=True):
            generate_python_code_bt = gr.Button(
                "Generate Python Code",
                elem_classes=["convert-btn"]
            )
        
        # Code display and action buttons
        with gr.Row(equal_height=True):
            with gr.Column():
                python = gr.Code(
                    label="Generated Python Code",
                    language="python",
                    lines=26,
                    elem_classes=["code-container"]
                )
                with gr.Row():
                    python_comment = gr.Button(
                        "Add Comments",
                        elem_classes=["run-btn", "py"]
                    )
                    python_run = gr.Button(
                        "Execute Code",
                        elem_classes=["run-btn", "cpp"]
                    )
        
        # Output section
        with gr.Row():
            result_out = gr.TextArea(
                label="Trading Recommendation",
                lines=8,
                elem_classes=["py-out"]
            )

        # Wire up event handlers
        generate_python_code_bt.click(
            handlers.on_generate_code,
            inputs=[model, crypto_currency, wallet_balance],
            outputs=[python]
        )
        python_comment.click(
            handlers.on_add_comments,
            inputs=[model, python],
            outputs=python
        )
        python_run.click(
            handlers.on_execute_code,
            inputs=[python],
            outputs=result_out
        )

    return ui
