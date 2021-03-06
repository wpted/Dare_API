import requests



class User:
    def __init__(self):
        self.id = User.__get_ip()
        self.dare_list = []

    @classmethod
    def __get_ip(cls) -> str:
        response = requests.get(url="https://ipinfo.io/json")
        response.raise_for_status()

        ip = response.json()["ip"]

        return ip



if __name__ == '__main__':
    ass = User("Ed")
    print(ass.id)

