import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class HttpRequest:
    def __init__(self):
        pass

    def get_session(self):
        retry_strategy = Retry(
            total=3,
            backoff_factor=4,
            status_forcelist=[500, 501, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)

        return http
