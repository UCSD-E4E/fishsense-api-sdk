from typing import List

import httpx

from fishsense_api_sdk.clients.client_base import ClientBase
from fishsense_api_sdk.models.image import Image


class ImageClient(ClientBase):
    def __init__(self, base_url: str, timeout: int):
        super().__init__(base_url, timeout)

    async def get(self, dive_id: int | None = None) -> Image | List[Image]:
        async with self._create_client() as client:
            if dive_id is not None:
                response = await client.get(f"/api/v1/dives/{dive_id}/images/")
                response.raise_for_status()
                return [Image.model_validate(image) for image in response.json()]
            else:
                raise NotImplementedError("Getting all images is not supported.")

    async def post_cluster(self, dive_id: int, image_ids: List[int]) -> int:
        async with self._create_client() as client:
            response = await client.post(
                f"/api/v1/dives/{dive_id}/images/clusters/",
                json=image_ids,
            )
            response.raise_for_status()
            return response.json()
