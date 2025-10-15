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

    async def get(self, camera_id: int | None = None) -> List[Camera] | Camera:
        async with self._create_client() as client:
            if camera_id is not None:
                response = await client.get(f"/api/v1/cameras/{camera_id}")
                response.raise_for_status()
                return Camera.model_validate(response.json())
            else:
                response = await client.get("/api/v1/cameras/")
                response.raise_for_status()
                return [Camera.model_validate(camera) for camera in response.json()]

    async def get_intrinsics(self, camera_id: int) -> CameraIntrinsics:
        async with self._create_client() as client:
            response = await client.get(f"/api/v1/cameras/{camera_id}/intrinsics/")
            response.raise_for_status()
            return CameraIntrinsics._from_internal(
                _CameraIntrinsics.model_validate(response.json())
            )

    async def post_intrinsics(
        self, camera_id: int, camera_intrinsics: CameraIntrinsics
    ) -> int:
        async with self._create_client() as client:
            response = await client.post(
                f"/api/v1/cameras/{camera_id}/intrinsics/",
                json=camera_intrinsics._to_internal().model_dump(),
            )
            response.raise_for_status()
            return response.json()
