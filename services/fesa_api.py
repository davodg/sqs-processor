from config import Config
from shared_libs.wrappers.http import HttpRequest


class FesaAPI(object):
    def __init__(self):
        self.config = Config()
        self.base_url = self.config.fesa_api_host
        self.http = HttpRequest().get_session()

    def get(self, path, params={}):
        endpoint = f"{self.base_url}{path}"

        try:
            status_code = None
            while not status_code or status_code >= 500:
                response = self.http.get(
                    endpoint, params=params)
                status_code = response.status_code

            response.raise_for_status()
            return response
        except Exception as e:
            error = dict({"error": e, "message": e.response.text})
            raise Exception(error)
    
    def post(self, path, payload):
        endpoint = f"{self.base_url}{path}"

        try:
            status_code = None
            while not status_code or status_code >= 500:
                response = self.http.post(
                    endpoint, json=payload)
                status_code = response.status_code

            response.raise_for_status()
            return response
        except Exception as e:
            error = dict({"error": e, "message": e.response.text})
            raise Exception(error)
    
    def put(self, path, payload, params={}):
        endpoint = f"{self.base_url}{path}"

        try:
            status_code = None
            while not status_code or status_code >= 500:
                response = self.http.put(
                    endpoint, json=payload, params=params)
                status_code = response.status_code

            response.raise_for_status()
            return response
        except Exception as e:
            error = dict({"error": e, "message": e.response.text})
            raise Exception(error)
    
    def delete(self, path, params={}):
        endpoint = f"{self.base_url}{path}"

        try:
            status_code = None
            while not status_code or status_code >= 500:
                response = self.http.delete(
                    endpoint, params=params)
                status_code = response.status_code

            response.raise_for_status()
            return response
        except Exception as e:
            error = dict({"error": e, "message": e.response.text})
            raise Exception(error)