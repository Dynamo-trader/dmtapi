from dmtapi import DMTAPI
from dmtapi.models.trade_model import TradeSetup, TakeProfit


async def trade_examples():
    api = DMTAPI(api_key="your_api_key", api_base_url="https://api.example.com")

    # Create a trade setup with multiple take profits
    setup = TradeSetup(
        symbol="EURUSD",
        volume=0.1,
        direction="buy",  # or "sell"
        entry_price=1.0500,  # Optional: if not provided, the current market price is used
        stop_loss=1.0500,
        take_profits=[
            TakeProfit(price=1.0600, close_pct=0.5, tp_as_pct=0, tp_as_pip=0),
            TakeProfit(
                price=0, close_pct=0.3, tp_as_pct=0.1, tp_as_pip=0
            ),  # 10% from entry
            TakeProfit(
                price=0, close_pct=0.2, tp_as_pct=0, tp_as_pip=50
            ),  # 50 pips from entry
        ],
    )

    # Open trade
    try:
        result = await api.trade.open(setup=setup, access_token="your_access_token")
        print("Trade opened successfully:", result)
    except ValueError as e:
        print(f"Invalid parameters: {e}")

    # Close a position
    try:
        close_result = await api.trade.close(
            ticket=12345, access_token="your_access_token"
        )
        print("Position closed:", close_result)
    except ValueError as e:
        print(f"Error closing position: {e}")
