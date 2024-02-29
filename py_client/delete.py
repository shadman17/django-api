import requests

product_id = input("Input the product ID")

try:
    product_id = int(product_id)
    
except:
    print(f'{product_id} is not valid')

if product_id:

    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"

    get_response = requests.delete(endpoint) # HTTP Request

    print(get_response.status_code)