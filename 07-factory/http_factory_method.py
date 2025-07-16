import http.client
from abc import ABC, abstractmethod


class HttpRequest(ABC):
    @abstractmethod
    def request(self, id: int) -> str:
        pass


class HttpGet(HttpRequest):
    def __init__(self, domain: str, path: str) -> None:
        self._domain = domain
        self._path = path

    def request(self, id: int) -> str:
        conn = http.client.HTTPConnection(self._domain)
        conn.request("GET", f"{self._path}/{id}")
        response = conn.getresponse()

        if response.status != 200:
            print(f"Error: {response.status} {response.reason}")
        else:
            data = response.read()
            conn.close()
            return data.decode("utf-8")

        conn.close()
        return ""


class HttpRequestFactory(ABC):
    def __init__(self, domain: str, path: str) -> None:
        self._domain = domain
        self._path = path

    @abstractmethod
    def create(self) -> HttpRequest:
        pass


class HttpGetFactory(HttpRequestFactory):
    def create(self) -> HttpRequest:
        return HttpGet(self._domain, self._path)


http_get_factory = HttpGetFactory("jsonplaceholder.typicode.com", "/posts")
http_get = http_get_factory.create()
print(http_get.request(1))
