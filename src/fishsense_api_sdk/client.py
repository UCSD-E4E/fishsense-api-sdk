""" "Main client for interacting with the Fishsense API."""

from fishsense_api_sdk.clients.camera_client import CameraClient
from fishsense_api_sdk.clients.dive_client import DiveClient
from fishsense_api_sdk.clients.image_client import ImageClient
from fishsense_api_sdk.clients.label_client import LabelClient


class Client:
    """Main client for interacting with the Fishsense API."""

    @property
    def cameras(self) -> CameraClient:
        """Get a list of camera instances .

        Returns:
            CameraClient: The camera client instance.
        """
        return self.__cameras

    @property
    def dives(self) -> DiveClient:
        """Get a list of dive instances .

        Returns:
            DiveClient: The dive client instance.
        """
        return self.__dives

    @property
    def images(self) -> ImageClient:
        """Get a list of image instances .

        Returns:
            ImageClient: The image client instance.
        """
        return self.__images

    @property
    def labels(self) -> LabelClient:
        """Get a list of label instances .

        Returns:
            LabelClient: The label client instance.
        """
        return self.__labels

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url

        self.__cameras = CameraClient(base_url, timeout)
        self.__dives = DiveClient(base_url, timeout)
        self.__images = ImageClient(base_url, timeout)
        self.__labels = LabelClient(base_url, timeout)
