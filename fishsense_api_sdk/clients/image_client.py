from typing import List

from fishsense_api_sdk.clients.client_base import ClientBase
from fishsense_api_sdk.models.dive_frame_cluster import DiveFrameCluster
from fishsense_api_sdk.models.image import Image


class ImageClient(ClientBase):
    def __init__(self, base_url: str, timeout: int):
        super().__init__(base_url, timeout)

    async def get(
        self, dive_id: int | None = None, image_id: int | None = None
    ) -> Image | List[Image]:
        async with self._create_client() as client:
            if dive_id is not None:
                response = await client.get(f"/api/v1/dives/{dive_id}/images/")
                response.raise_for_status()
                return [Image.model_validate(image) for image in response.json()]
            elif image_id is not None:
                response = await client.get(f"/api/v1/images/{image_id}")
                response.raise_for_status()
                return Image.model_validate(response.json())
            else:
                raise NotImplementedError("Getting all images is not supported.")

    async def get_clusters(self, dive_id: int) -> List[DiveFrameCluster]:
        async with self._create_client() as client:
            response = await client.get(f"/api/v1/dives/{dive_id}/images/clusters/")
            response.raise_for_status()
            return [
                DiveFrameCluster.model_validate(cluster) for cluster in response.json()
            ]

    async def post_cluster(self, dive_id: int, image_ids: List[int]) -> int:
        async with self._create_client() as client:
            response = await client.post(
                f"/api/v1/dives/{dive_id}/images/clusters/",
                json=image_ids,
            )
            response.raise_for_status()
            return response.json()
