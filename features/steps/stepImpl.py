import json

import requests
from behave import *

from utils import payload
from utils.configurations import *
from utils.headers import Headers
from utils.resources import Resources


@given('the Book Details with Book name :: {bookName}, ISBN :: {isbn}, Aisle :: {aisle} and Author :: {authorName} '
       'which need to be added to the Library')
def step_addBookIMPL(context, bookName, isbn, aisle, authorName):
    # Load your configuration for the test #
    config = getConfig()
    context.endpoint = config['API']['baseurl'] + Resources().get_addBookResource()


@when('we execute AddBook POST API with data :: {bookName} , {isbn}, {aisle} and {authorName}')
def step_addBookIMPL(context, bookName, isbn, aisle, authorName):
    context.response = requests.post(url=context.endpoint,
                                     json=payload.addBookPayload(bookName, isbn, aisle, authorName),
                                     headers=Headers().get_content_json())


@then('book is successfully added')
def step_addBookIMPL(context):
    json_response = context.response.json()
    context.book_id = json_response['ID']
    assert context.book_id, 'Book already exists !'
    print(f'The response :: {json.dumps(json_response, indent=2)}')
