import requests

endpoint = "http://localhost:8000/api/products/3/"

get_response = requests.get(endpoint, json={"title": "Helllow", 'content': 'this is bla bla', 'price': 1234 }) # HTTP Request

print(get_response.json())