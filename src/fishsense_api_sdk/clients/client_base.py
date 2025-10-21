"""Base client for interacting with the Fishsense API."""

from abc import ABC

import httpx


class ClientBase(ABC):
    # pylint: disable=too-few-public-methods
    """Base client for interacting with the Fishsense API."""

    def __init__(self, base_url: str, timeout):
        self.base_url = base_url
        self.timeout = timeout

    def _create_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout)
