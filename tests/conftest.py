import pytest
import requests
from test_data.TestData import Status, Reason, Others, Keys

@pytest.fixture(scope="class")
def fixture_conf(request):
    url = 'https://www.googleapis.com/blogger/v3/blogs/920308070457707190'
    # if request.param
    res = requests.get(url + request.param)
    request.cls.res=res
    yield

@pytest.fixture(scope="class")
def fixture_conf_post(request):
    url = 'https://www.googleapis.com/blogger/v3/blogs/920308070457707190/posts'
    myobj = {
        "kind": "blogger#post",
        "blog": {
            "id": "920308070457707190"
        },
        "title": "A new post",
        "content": "With <b>exciting</b> content..."
    }
    res = requests.post(url, json=myobj, headers=Others().key)
    request.cls.res=res
    yield