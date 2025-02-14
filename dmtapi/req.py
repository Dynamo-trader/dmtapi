import aiohttp
from typing import Union, Any, Optional
from urllib.parse import urlencode
from functools import lru_cache


class RequestMaker:
    def __init__(self):
        self.api_base_url = "https://api.dmtmarkets.com"
        self.connector = aiohttp.TCPConnector(
            limit=100,
            ttl_dns_cache=300,
            use_dns_cache=True
        )

        self.session = aiohttp.ClientSession(
            connector=self.connector,
            timeout=aiohttp.ClientTimeout(total=60),
            headers={
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json"
            }
        )

    @lru_cache(maxsize=100)
    def build_url(self, url: str, params: Optional[dict] = None) -> str:
        url = f"{self.api_base_url}/{url}"
        if not params:
            return url
        filtered_params = {k: v for k, v in params.items() if v is not None}
        return f"{url}?{urlencode(filtered_params)}"

    @staticmethod
    @lru_cache(maxsize=100)
    def get_headers(
        extra_headers: Optional[dict] = None,
        access_token: Optional[str] = None,
        login: Optional[int] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> dict:
        headers = {}

        if access_token:
            headers["ACCESS-TOKEN"] = access_token

        if login and server:
            headers["TRADER-LOGIN"] = str(login)
            headers["TRADER-SERVER"] = server

        if api_key:
            headers["USER-API-KEY"] = api_key

        if extra_headers:
            headers.update(extra_headers)

        return headers

    async def get(
        self,
        url: str,
        params: Optional[dict[str, str]] = None,
        extra_headers: Optional[dict] = None,
        access_token: Optional[str] = None,
        login: Optional[str] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> Any:
        full_url = self.build_url(url, params)
        headers = self.get_headers(
            extra_headers=extra_headers,
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key
        )

        async with self.session.get(full_url, headers=headers) as response:
            response.raise_for_status()
            return await response.json()

    async def post(
        self,
        url: str,
        params: Optional[dict[str, str]] = None,
        data: Optional[Union[dict, str]] = None,
        json: Optional[Union[dict, str]] = None,
        extra_headers: Optional[dict] = None,
        access_token: Optional[str] = None,
        login: Optional[int] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,

    ) -> Any:
        full_url = self.build_url(url, params)
        headers = self.get_headers(
            extra_headers=extra_headers,
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key,
        )

        async with self.session.post(full_url, data=data, json=json, headers=headers) as response:
            response.raise_for_status()
            return await response.json()

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()
