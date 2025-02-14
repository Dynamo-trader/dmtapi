from typing import Optional
from dmtapi.models.account_model import TraderInfo
from dmtapi.models.trade_model import TradeSetup
from dmtapi.req import RequestMaker


class DMTAPI:
    """
    Main class for interacting with the DMT trading API.

    This class provides methods to manage trading accounts and execute trades.

    Args:
        api_key (str): The API key for authentication.
    """

    request = RequestMaker()

    def __init__(self, api_key: str):
        self.api_key = api_key

    async def get_account_info(
            self,
            access_token: Optional[str] = None,
            login: Optional[str] = None,
            server: Optional[str] = None,
            api_key: Optional[str] = None
    ) -> TraderInfo:
        """
        Retrieve information about a specific trading account.

        Args:
            access_token (Optional[str]): Account access token. Required if login and server are not provided.
            login (Optional[str]): Account login. Required if access_token is not provided.
            server (Optional[str]): Trading server. Required if access_token is not provided.
            api_key (Optional[str]): Override default API key.

        Returns:
            TraderInfo: Object containing account information.

        Raises:
            ValueError: If neither access_token nor both login and server are provided.
        """
        if not access_token and (not login or not server):
            raise ValueError("Access token or login and server must be provided")

        r = await self.request.get(
            url="/account/info",
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key or self.api_key
        )

        return TraderInfo(**r)

    async def get_all_accounts(self, api_key: Optional[str] = None) -> list[TraderInfo]:
        """
        Retrieve information about all available trading accounts.

        Args:
            api_key (Optional[str]): Override default API key.

        Returns:
            list[TraderInfo]: List of objects containing account information.
        """
        r = await self.request.get(
            url="/account/all",
            api_key=api_key or self.api_key
        )

        return [TraderInfo(**i) for i in r]

    async def open_trade(
        self,
        setup: TradeSetup,
        access_token: str,
        login: int,
        server: str,
        api_key: Optional[str] = None
    ) -> list[dict]:
        """
        Open a new trade based on the provided setup.

        Args:
            setup (TradeSetup): Trade configuration including symbol, volume, direction, etc.
            access_token (str): Account access token.
            login (int): Account login number.
            server (str): Trading server.
            api_key (Optional[str]): Override default API key.

        Returns:
            list[dict]: List of trade results.
            If you have multiple tp it returns multiple trades as MT5 doesn't support more than one tp on a trade.
            So it splits the volume and opens multiple trades with the same entry, sl and tp.
        """
        r = await self.request.post(
            url="/trade/open",
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key or self.api_key,
            data=setup.model_dump()
        )

        return r
