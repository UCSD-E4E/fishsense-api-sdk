from typing import List

from fishsense_api_sdk.clients.client_base import ClientBase
from fishsense_api_sdk.models.dive import Dive


class DiveClient(ClientBase):
    def __init__(self, base_url: str, timeout: int):
        super().__init__(base_url, timeout)

    async def get(self, dive_id: int | None = None) -> Dive | List[Dive]:
        async with self._create_client() as client:
            if dive_id is not None:
                response = await client.get(f"/api/v1/dives/{dive_id}")
                response.raise_for_status()
                return Dive.model_validate(response.json())
            else:
                response = await client.get("/api/v1/dives/")
                response.raise_for_status()
                return [Dive.model_validate(dive) for dive in response.json()]
