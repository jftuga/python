import requests

class make_http_request():
    def __init__(self, url):
        self.response = requests.get(url)

