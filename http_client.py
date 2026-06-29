import requests

class HttpClient:

    def __init__(self, site: str):
        if site == "dog":
            self.url = "https://dog.ceo"
        elif site == "openbrewerydb":
            self.url = "https://api.openbrewerydb.org"
        elif site == "jsonplaceholder":
            self.url = "https://jsonplaceholder.typicode.com"
        else:
            self.url = site

    def request(self, method: str, path: str, body: dict|None = None, code: int = 200, params: dict|str|None = None) -> dict:
        response = requests.request(method, f"{self.url}/{path}", data=body, params=params)
        assert response.status_code == code, f"The server returned an unexpected response code: {response.status_code}"
        return response.json()

    def check_request(self, code: int = 200) -> None:
        response = requests.request("GET", f"{self.url}/")
        assert response.status_code == int(code), f"The server returned an unexpected response code: {response.status_code}"

    def get(self, path: str, code: int = 200, params: dict|str|None = None):
        return self.request('GET', path=path, code=code, params=params)

    def post(self, path: str, body: dict|None = None, code: int = 201) :
        return self.request('POST', path=path, body=body, code=code)

    def put(self, path: str, body: dict|None = None, code: int = 200) :
        return self.request('PUT', path=path, body=body, code=code)

    def patch(self, path: str, body: dict|None = None, code: int = 200) :
        return self.request('PATCH', path=path, body=body, code=code)

    def delete(self, path: str, code: int = 200) :
        return self.request('DELETE', path=path, code=code)
