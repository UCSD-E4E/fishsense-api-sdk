from typing import List

import httpx

from fishsense_api_sdk.clients.client_base import ClientBase
from fishsense_api_sdk.models.dive import Dive


class DiveClient(ClientBase):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    async def get(self) -> List[Dive]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/api/v1/dives/")
            response.raise_for_status()
            return [Dive.model_validate(dive) for dive in response.json()]
