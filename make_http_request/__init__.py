import requests

class make_http_request():
    __title__ = "make_http_request"
    __description__ = "HTTP requester with retry"
    __url__ = "https://github.com/jftuga/python"
    __version__ = "0.1.1"
    
    def __init__(self, url):
        self.response = requests.get(url)
