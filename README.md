# Crypto Trading Strategy Generator

An AI-powered application that generates Python trading strategies for cryptocurrencies. The application uses various AI models to create executable Python code that analyzes crypto market data and provides buy/sell recommendations.

DISCLAIMER: This application is for educational purposes only on how to use LLMs to generate trading code and compare results against each other. This is not to be used as trading advice.

## Features

- 🤖 **Multiple AI Models**: Support for GPT-5, Gemini 2.5 Pro, and open source models via Ollama (local) and Groq
- 💱 **Multi-Currency Support**: Generate strategies for BTC, ETH, SOL, and ADA
- 📊 **Real-time Market Data**: Fetches live data from Binance API
- 🎯 **Confidence-Based Recommendations**: Adjusts trade amounts based on prediction confidence
- 💬 **Code Documentation**: Automatically add comments and docstrings to generated code
- ▶️ **Live Execution**: Execute generated strategies directly in the UI
- 🎨 **User-Friendly Interface**: Built with Gradio for easy interaction

## Prerequisites

- Python 3.11 or higher
- API keys for AI services (optional, depending on which models you use):
  - OpenAI API key (for GPT models)
  - Google API key (for Gemini models)
  - Groq API key (for Groq models)
- Ollama installed locally (optional, for local models)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd trading_strategy_generator
```

2. Install dependencies using `uv` (recommended) or `pip`:

**Using uv:**
```bash
uv sync
```

**Using pip:**
```bash
pip install -r requirements.txt
# or
pip install gradio numpy ollama openai pandas python-dotenv requests
```

3. Create a `.env` file in the project root with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

1. Start the application:
```bash
uv run main.py
```

2. The application will launch in your default browser automatically.

3. Configure your strategy:
   - Select a cryptocurrency (BTC, ETH, SOL, or ADA)
   - Set your wallet balance in USDT
   - Choose an AI model

4. Click "Generate Python Code" to create a trading strategy

5. Optional actions:
   - Click "Add Comments" to enhance code documentation
   - Click "Execute Code" to run the strategy and see recommendations

## Project Structure

```
trading_strategy_generator/
├── main.py                 # Application entry point
├── pyproject.toml          # Project dependencies and metadata
├── config/
│   └── settings.py         # Configuration and environment variables
├── prompts/
│   └── templates.py        # AI prompt templates
├── services/
│   ├── ai_client.py        # AI client management
│   └── code_generator.py   # Code generation logic
├── styles/
│   └── styles.py           # UI styling
├── ui/
│   ├── components.py       # Gradio UI components
│   └── handlers.py         # UI event handlers
└── utils/
    └── executor.py         # Code execution utilities
```

## How It Works

1. **Strategy Generation**: The AI model generates Python code that:
   - Fetches real-time price data from Binance API
   - Analyzes market indicators (price change, volume, etc.)
   - Determines buy/sell recommendation
   - Calculates recommended trade amount based on confidence level

2. **Execution**: The generated code can be executed directly to:
   - Get current market data
   - Provide trading recommendations (BUY/SELL)
   - Suggest trade amounts in USDT

3. **Documentation**: Add detailed comments and docstrings to understand the generated strategy logic.

## Supported AI Models

- **gpt-5**: OpenAI's latest model (requires OpenAI API key)
- **gemini-2.5-pro**: Google's Gemini model (requires Google API key)
- **gpt-oss:20b**: Open-source model via Groq (requires Groq API key)
- **openai/gpt-oss-120b**: Larger open-source model via Groq (requires Groq API key)

## Configuration

Edit `config/settings.py` to customize:
- Default cryptocurrency
- Default wallet balance
- Default AI model
- Available currencies and models
- API endpoints

## Example Output

The generated trading strategy will provide recommendations like:
```
Recommendation: BUY
Amount: 750.00 USDT
Confidence: High
Current Price: 116,719.99 USDT
Reason: Strong upward trend with high volume
```

## Security Notes

- Never commit your `.env` file with actual API keys
- Be cautious when executing generated code
- The application is for educational purposes - do not follow trading advice.
- Start with small amounts when testing strategies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for educational and research purposes only. Cryptocurrency trading involves substantial risk of loss. The generated strategies should not be considered financial advice. Always do your own research and consult with financial professionals before making investment decisions.
