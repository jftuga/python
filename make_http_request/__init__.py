import requests

__title__ = "make_http_request"
__description__ = "HTTP requester with retry"
__url__ = "https://github.com/jftuga/python"
__version__ = "0.1.0"

class make_http_request():
    def __init__(self, url):
        self.response = requests.get(url)
