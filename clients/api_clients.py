from httpx import Client, URL, QueryParams, Response
from httpx._types import RequestData, RequestFiles
from typing import Any


class APIClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        return self.client.get(url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        return self.client.delete(url)