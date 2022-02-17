import os

import requests
import json
import tempfile
import pytest

from src.api import app
from src.logger import logger

URL = 'http://127.0.0.1:5000/tasks/'

"""
@pytest.mark.positive -> test will be marked as positive (specified by requirement)
@pytest.mark.signle_task -> URL/tasks/1/, the return type JSON, data is populated
"""

"""
{
    "tasks": [{
        "completed": 0,
        "content": "Rustam Test 1",
        "date_created": "Thu, 17 Feb 2022 11:21:23 GMT",
        "id": 2
    }
}

{"completed":0,"content":"Rustam Test 1","date_created":"Thu, 17 Feb 2022 11:21:23 GMT","id":2}
"""


@pytest.mark.check_status_code
def test_base_url_status_code_200():
    get_the_list = requests.get(URL)
    assert get_the_list.status_code == 200, "Status code is not 200"


@pytest.mark.check_status_code
def test_base_url_status_code_404_with_negative_id():
    get_the_list = requests.get(URL + '-1')
    assert get_the_list.status_code == 404, "Status code is not 404"


@pytest.mark.check_content_type
def test_header_content_type():
    get_the_list = requests.get(URL)
    assert get_the_list.headers['Content-Type'] == 'application/json', "Content-Type is not application/json"


@pytest.mark.check_content_type
def test_header_content_type_with_negative_id():
    get_the_list = requests.get(URL + '-1')
    assert get_the_list.headers['Content-Type'] == 'application/json', "Content-Type is not application/json"


@pytest.mark.positive
def test_get_the_task_with_id_1_exist():
    get_the_list = requests.get(URL + '2')
    assert get_the_list.status_code == 200, "Status code is not 200"


@pytest.mark.positive
def test_get_the_task_with_id_1_exist_status_code():
    get_the_list = requests.get(URL + '2')
    assert get_the_list.headers['Content-Type'] == 'application/json', "Content-Type is not application/json"


@pytest.mark.signle_task
def test_get_the_task_with_id_1_exist_content():
    get_the_list = requests.get(URL + '2').json()
    assert get_the_list['completed'] == 0
    assert get_the_list['content'] == 'Rustam Test 1'
    assert get_the_list['date_created'] == 'Thu, 17 Feb 2022 11:21:23 GMT'
    assert get_the_list['id'] == 2


