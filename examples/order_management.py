from dmtapi import DMTAPI


async def order_examples():
    api = DMTAPI(api_key="your_api_key", api_base_url="https://api.example.com")

    # Get trade history
    history = await api.order.history(access_token="your_access_token")
    print("Trade history:", history)

    # Get pending orders
    pending = await api.order.pending(access_token="your_access_token")
    print("Pending orders:", pending)

    # Get open positions
    positions = await api.order.positions(access_token="your_access_token")
    for position in positions:
        print(f"Position {position.ticket}: {position.symbol} {position.volume}")
