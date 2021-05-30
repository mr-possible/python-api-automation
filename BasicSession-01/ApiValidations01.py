import json

import requests

url = 'http://216.10.245.166/Library/GetBook.php'
user_dict = {'AuthorName': 'Rahul Shetty2'}

response = requests.get(url, params=user_dict)

# Notice the pretty-printing approach
print(f'The content of the response :: {json.dumps(response.json(), indent=2)}')
print(f'The type response :: {type(response.json())}')

assert response.status_code is 200
print(f'Status code :: {response.status_code}')

print(f'Headers :: {response.headers}')
assert response.headers.get('Content-Type') == 'application/json;charset=UTF-8'
