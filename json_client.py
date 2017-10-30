##JSON

import requests

data = {'key': 1}
# POST some form-encoded data:
print('json')
response = requests.get(url='http://127.0.0.1:5000/rfq', params=data)
print(response)