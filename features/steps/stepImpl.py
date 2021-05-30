import json

import requests
from behave import *

from utils import payload
from utils.configurations import *
from utils.headers import Headers
from utils.resources import Resources


@given('the Book Details which need to be added to the Library')
def step_addBookIMPL(context):
    # Load your configuration for the test #
    config = getConfig()
    context.endpoint = config['API']['baseurl'] + Resources().get_addBookResource()


@when('we execute AddBook POST API')
def step_addBookIMPL(context):
    context.response = requests.post(url=context.endpoint,
                                     json=payload.addBookPayload(),
                                     headers=Headers().get_content_json())


@then('book is successfully added')
def step_addBookIMPL(context):
    json_response = context.response.json()
    context.book_id = json_response['ID']
    assert context.book_id, 'Book already exists !'
    print(f'The response :: {json.dumps(json_response, indent=2)}')
