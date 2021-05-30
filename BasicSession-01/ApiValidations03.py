import json
from utils import payload
import requests
from utils.configurations import *
from utils.resources import Resources
from utils.headers import Headers

## Load your configuration for the test ##
config = getConfig()

## API Test to add book to the database ##
endpoint = config['API']['baseurl'] + Resources().get_addBookResource()
response = requests.post(url=endpoint,
                         json=payload.addBookPayload(),
                         headers=Headers().get_content_json())
json_response = response.json()

print(f'The response :: {json.dumps(json_response, indent=2)}')
