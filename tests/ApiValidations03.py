import json
import os
import requests
from utils import payload
from utils.resources import Resources
from utils.headers import Headers
from dotenv import load_dotenv

load_dotenv()

# API Test to add book to the database ##
endpoint = os.environ.get('baseurl') + Resources().get_addBookResource()
response = requests.post(url=endpoint,
                         json=payload.addBookPayload("test", "1234FB", "Fiction", "JK Rowling"),
                         headers=Headers().get_content_json())
json_response = response.json()

print(f'The response :: {json.dumps(json_response, indent=2)}')