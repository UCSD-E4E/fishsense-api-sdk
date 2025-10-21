"""Client for interacting with label-related endpoints of the Fishsense API."""

from fishsense_api_sdk.clients.client_base import ClientBase
from fishsense_api_sdk.models.laser_label import LaserLabel
from fishsense_api_sdk.models.species_label import SpeciesLabel


class LabelClient(ClientBase):
    """Client for interacting with label-related endpoints of the Fishsense API."""

    def __init__(self, base_url: str, timeout: int):
        super().__init__(base_url, timeout)

    async def get_laser_label(self, image_id: int) -> LaserLabel:
        """Get a LaserLabel by its ID .

        Args:
            image_id (int): The ID of the image to retrieve the laser label for.

        Returns:
            LaserLabel: The laser label for the specified image.
        """
        async with self._create_client() as client:
            response = await client.get(f"/api/v1/labels/laser/{image_id}")
            response.raise_for_status()
            return LaserLabel.model_validate(response.json())

    async def get_species_label(self, image_id: int) -> SpeciesLabel:
        """Get a species label .

        Args:
            image_id (int): The ID of the image to retrieve the species label for.

        Returns:
            SpeciesLabel: The species label for the specified image.
        """
        async with self._create_client() as client:
            response = await client.get(f"/api/v1/labels/species/{image_id}")
            response.raise_for_status()
            return SpeciesLabel.model_validate(response.json())

    async def post_species_label(
        self, image_id: int, species_label: SpeciesLabel
    ) -> int:
        """Post a species label to an image .

        Args:
            image_id (int): The ID of the image to post the species label to.
            species_label (SpeciesLabel): The species label to post.

        Returns:
            int: The ID of the created species label.
        """
        async with self._create_client() as client:
            response = await client.post(
                f"/api/v1/labels/species/{image_id}",
                json=species_label.model_dump(),
            )
            response.raise_for_status()
            return response.json()
