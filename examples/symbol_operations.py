from dmtapi import DMTAPI


async def symbol_examples():
    api = DMTAPI(api_key="your_api_key", api_base_url="https://api.example.com")

    # Get symbol price
    price = await api.symbol.price(symbol="EURUSD", access_token="your_access_token")
    print(f"Current EURUSD price: {price.ask}/{price.bid}")

    # Get symbol information
    symbol_info = await api.symbol.info(
        symbol="EURUSD", access_token="your_access_token"
    )
    print(f"Symbol specifications: {symbol_info}")

    # Get all available symbols
    symbols = await api.symbol.all(access_token="your_access_token")
    print("Available symbols:", symbols)
