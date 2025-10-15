from fishsense_api_sdk.clients.dive_client import DiveClient
from fishsense_api_sdk.clients.image_client import ImageClient


class Client:
    @property
    def dives(self) -> DiveClient:
        return self.__dives

    @property
    def images(self) -> ImageClient:
        return self.__images

    def __init__(self, base_url: str):
        self.base_url = base_url

        self.__dives = DiveClient(base_url)
        self.__images = ImageClient(base_url)
