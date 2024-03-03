import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title": "Helllo me!", 'content': 'this is bla bla 2', 'price': 12346 }

get_response = requests.post(endpoint, json=data) # HTTP Request


print(get_response.json())