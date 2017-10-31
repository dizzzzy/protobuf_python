##JSON

import requests

# GET some form-encoded data:
response = requests.get(url='http://127.0.0.1:5002/rfq/1&2&4&sports&5')
print(response.json())
response = requests.get(url='http://127.0.0.1:5002/rfq/1&2&4&education&5')
print(response.json())
response = requests.get(url='http://127.0.0.1:5002/rfq/1&2&4&sports&20000')
print(response.json())
response = requests.get(url='http://127.0.0.1:5002/rfq/1&2&4&education&5')
print(response.json())
response = requests.get(url='http://127.0.0.1:5002/rfq/1&2&4&education&5')
print(response.json())
