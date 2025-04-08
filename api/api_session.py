from requests import Session
import requests
from utils.utils import log_api_call  # или откуда ты его поместишь

class TestSession(Session):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url

    @log_api_call
    def demoshop_api_request(self, path, method='POST', *args, **kwargs):
        full_url = self.base_url + path
        return requests.request(url=full_url, method=method, *args, **kwargs)