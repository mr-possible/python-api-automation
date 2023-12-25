import json, os
import requests
from dotenv import load_dotenv
from utils import payload

from utils.headers import Headers
from utils.resources import Resources

load_dotenv()


def after_scenario(context, scenario):
    endpoint = os.environ.get('baseurl') + Resources().get_deleteBookResource()
    response = requests.post(url=endpoint,
                             json=payload.delete_book_payload(context.book_id),
                             headers=Headers().get_content_json())
    json_response = response.json()
    assert json_response['msg'] == 'book is successfully deleted'
    print(f'The response :: {json.dumps(json_response, indent=2)}')
