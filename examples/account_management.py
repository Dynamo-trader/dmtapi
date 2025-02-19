from dmtapi import DMTAPI


async def account_examples():
    # Initialize the API
    api = DMTAPI(api_key="your_api_key", api_base_url="https://api.example.com")

    # Get specific account information
    account_info = await api.account.info(access_token="your_access_token")
    print(f"Account Balance: {account_info.balance}")
    print(f"Account Equity: {account_info.equity}")

    # Get all accounts
    all_accounts = await api.account.all()
    for account in all_accounts:
        print(f"Account {account.login} on {account.server}")
