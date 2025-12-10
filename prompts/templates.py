"""Prompt templates for code generation."""

SYSTEM_MESSAGE = """
You are an effective programming assistant specialized to generate Python code based on the inputs.
Respond only with Python code; use comments sparingly and do not provide any explanation other than occasional comments.
Do not include Markdown formatting (```), language tags (python), or extra text.
"""


def get_trade_code_prompt(currency: str, wallet_balance: float) -> str:
    """Generate prompt for trading code generation."""
    return f"""
        Create a simple Crypto trading engine Python code.
        The engine will sell or buy the given crypto currency against USDT (Tether) based on the available wallet balance
        This should be a simple Python code, not a function
        The currency is: {currency}
        The wallet balance is: {wallet_balance}
        Output will be a text containing the followings:
            - Advice to sell or buy
            - Amount in USDT
            - Confidence
            - Current Price
            - Reason
            Example output:
            {{
                Recommendation: BUY
                Amount: 750.00 USDT
                Confidence: High
                Current Price: 116,719.99 USDT
                Reason: Strong upward trend with high volume
            }}
        Rules you have to apply in the code:
            - compose symbol: convert the input `currency` argument to upper case and concatenate it to string "USDT"
            - compose url passing the previously composed symbol: `url = f"https://data-api.binance.vision/api/v3/ticker/24hr?symbol={{symbol}}`
            - call the api from with this url, expect to get the following json response, for example:
                {{'symbol': 'BTCUSDT',
                'priceChange': '1119.99000000',
                'priceChangePercent': '0.969',
                'weightedAvgPrice': '116314.23644195',
                'prevClosePrice': '115600.00000000',
                'lastPrice': '116719.99000000',
                'lastQty': '0.05368000',
                'bidPrice': '116719.99000000',
                'bidQty': '2.81169000',
                'askPrice': '116720.00000000',
                'askQty': '3.46980000',
                'openPrice': '115600.00000000',
                'highPrice': '117286.73000000',
                'lowPrice': '114737.11000000',
                'volume': '12500.51369000',
                'quoteVolume': '1453987704.98443060',
                'openTime': 1758015394001,
                'closeTime': 1758101794001,
                'firstId': 5236464586,
                'lastId': 5238628513,
                'count': 2163928}}
            - build a logic based on the retrieving values which can decide whether the engine should sell or buy the given crypto currency
                - in the logic the code should also decide what is the confidence level of selling or buying.
                    - if the confidence level is high the `amount` should be higher (closer to the `current_wallet_balance`)
                    - if the confidence level is lower then the amount should be lower as well
            - error handling:
                - if the api call returns with a json having `code`, `msg` keys in it (eg. 'code': -1121, 'msg': 'Invalid symbol.') then handle this error message
        Response rule: in your response do not include Markdown formatting (```), language tags (python), or extra text.
    """


def get_docstring_prompt(python_code: str) -> str:
    """Generate prompt for adding docstrings to code."""
    return f"""
        Consider the following Python code: \n\n
        {python_code} \n\n

        Generate a docstring comment around this code and small comments alongside with the Python code. \n
        Response rule: in your response do not include Markdown formatting (```), language tags (python), or extra text.
    """


def build_messages(user_message: str) -> list:
    """Build message array for AI completion."""
    return [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": user_message}
    ]
