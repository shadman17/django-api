import requests

endpoint = "http://localhost:8000/api/products/3/update"

data = {
    "title" : "Hello World my old friend",
    "price": 1232.00
}

get_response = requests.put(endpoint, json=data) # HTTP Request

print(get_response.json())