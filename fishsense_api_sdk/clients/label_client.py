from fishsense_api_sdk.clients.client_base import ClientBase
from fishsense_api_sdk.models.laser_label import LaserLabel
from fishsense_api_sdk.models.species_label import SpeciesLabel


class LabelClient(ClientBase):
    def __init__(self, base_url: str, timeout: int):
        super().__init__(base_url, timeout)

    async def get_laser_label(self, image_id: int) -> LaserLabel:
        async with self._create_client() as client:
            response = await client.get(f"/api/v1/labels/laser/{image_id}")
            response.raise_for_status()
            return LaserLabel.model_validate(response.json())

    async def get_species_label(self, image_id: int) -> SpeciesLabel:
        async with self._create_client() as client:
            response = await client.get(f"/api/v1/labels/species/{image_id}")
            response.raise_for_status()
            return SpeciesLabel.model_validate(response.json())

    async def post_species_label(
        self, image_id: int, species_label: SpeciesLabel
    ) -> int:
        async with self._create_client() as client:
            response = await client.post(
                f"/api/v1/labels/species/{image_id}",
                json=species_label.model_dump(),
            )
            response.raise_for_status()
            return response.json()
