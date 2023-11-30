import json

import requests

url = 'http://216.10.245.166/Library/GetBook.php'
user_dict = {'AuthorName': 'Rahul Shetty2'}

response = requests.get(url, params=user_dict)
json_response = response.json()

expected_result = {
    "book_name": "Devops",
    "isbn": "abc123xyy9",
    "aisle": "75"
}

for book in json_response:
    if book['isbn'] == 'abc123xyy9':
        print(f'The book details in our response are :: {json.dumps(book, indent=2)}')
        assert book == expected_result
        break