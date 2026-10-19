import pytest
import requests

@pytest.fixture
def input_data():
    r = requests.get('https://www.python.org')
    return r.status_code

def test_get_url(input_data):
    assert input_data == 200