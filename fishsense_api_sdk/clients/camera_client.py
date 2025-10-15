from typing import List

from fishsense_api_sdk.clients.client_base import ClientBase
from fishsense_api_sdk.models.camera import Camera
from fishsense_api_sdk.models.camera_intrinsics import (
    CameraIntrinsics,
    _CameraIntrinsics,
)


class CameraClient(ClientBase):
    def __init__(self, base_url: str, timeout: int):
        super().__init__(base_url, timeout)

    async def get(self) -> List[Camera]:
        async with self._create_client() as client:
            response = await client.get("/api/v1/cameras/")
            response.raise_for_status()
            return [Camera.model_validate(camera) for camera in response.json()]

    async def post_intrinsincs(
        self, camera_intrinsics: CameraIntrinsics
    ) -> CameraIntrinsics:
        async with self._create_client() as client:
            response = await client.post(
                "/api/v1/cameras/intrinsics/",
                json=camera_intrinsics._to_internal().model_dump(),
            )
            response.raise_for_status()
            return CameraIntrinsics._from_internal(
                _CameraIntrinsics.model_validate(response.json())
            )
