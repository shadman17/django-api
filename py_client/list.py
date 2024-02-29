import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title": "Helllow", 'content': 'this is bla bla', 'price': 1234 }

get_response = requests.get(endpoint) # HTTP Request


print(get_response.json())