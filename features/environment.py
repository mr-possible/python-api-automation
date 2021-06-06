import json

import requests

from utils import payload
from utils.configurations import getConfig
from utils.headers import Headers
from utils.resources import Resources


def after_scenario(context, scenario):
    # Run this based on specific tags
    # Load your configuration for the test ##
    config = getConfig()

    # API Test to add book to the database ##
    endpoint = config['API']['baseurl'] + Resources().get_deleteBookResource()
    response = requests.post(url=endpoint,
                             json=payload.deleteBookPayload(context.book_id),
                             headers=Headers().get_content_json())
    json_response = response.json()
    assert json_response['msg'] == 'book is successfully deleted'
    print(f'The response :: {json.dumps(json_response, indent=2)}')
