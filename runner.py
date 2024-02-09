from make_http_request import make_http_request

req = make_http_request("https://example.com")
print(req.response.text)
