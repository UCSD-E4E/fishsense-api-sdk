from typing import List

import httpx

from fishsense_api_sdk.clients.client_base import ClientBase
from fishsense_api_sdk.models.image import Image


class ImageClient(ClientBase):
    def __init__(self, base_url: str):
        super().__init__(base_url)
