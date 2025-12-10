"""Main entry point for the Crypto Trading Strategy Generator."""
from ui.components import create_ui


def main():
    """Launch the trading strategy generator application."""
    ui = create_ui()
    ui.launch(inbrowser=True)


if __name__ == "__main__":
    main()
