import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/" #"http://127.0.0.1:8000/"
endpoint1 = "http://localhost:8000/api"

get_response = requests.get(endpoint1, json={'query':'Hello World'}) #
print(get_response.text)
print(get_response.json())
print(get_response.status_code)

