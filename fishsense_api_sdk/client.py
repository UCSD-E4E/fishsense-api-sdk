from fishsense_api_sdk.clients.dive_client import DiveClient


class Client:
    @property
    def dives(self) -> DiveClient:
        return self.__dives

    def __init__(self, base_url: str):
        self.base_url = base_url

        self.__dives = DiveClient(base_url)
