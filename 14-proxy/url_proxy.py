from abc import ABC, abstractmethod
import http.client


class Request(ABC):
    @abstractmethod
    def get(self, id: int) -> str:
        pass


class GetRequest(Request):
    def __init__(self, domain: str, path: str):
        self.__domain = domain
        self.__path = path

    def get(self, id: int):
        print("Se va al servicio")
        conn = http.client.HTTPConnection(self.__domain)
        conn.request("GET", "/" + self.__path + "/" + str(id))
        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            conn.close()
            return data.decode("utf-8")
        else:
            conn.close()
            return f"Error: {response.status}"


class CacheGetRequest(Request):
    def __init__(self, request: GetRequest):
        self.__request = request
        self.__cache = {}

    def get(self, id: int) -> str:
        if id in self.__cache:
            print("Se va al cache")
            return self.__cache[id]
        else:
            data = self.__request.get(id)
            self.__cache[id] = data
            return data


get_request = GetRequest("jsonplaceholder.typicode.com", "posts")
# print(get_request.get(1))
# print(get_request.get(1))

cache_get_request = CacheGetRequest(get_request)
print(cache_get_request.get(1))
print(cache_get_request.get(1))
print(cache_get_request.get(2))
print(cache_get_request.get(2))
