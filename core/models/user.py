import requests



class User:
    def __init__(self, name):
        self.name = name
        self.id = User.__get_ip()


    @classmethod
    def __get_ip(cls) -> str:
        response = requests.get(url="https://ipinfo.io/json")
        response.raise_for_status()

        ip = response.json()["ip"]

        return ip



if __name__ == '__main__':
    ass = User("Ed")
    print(ass.id)
    print(ass.dare_dict)
