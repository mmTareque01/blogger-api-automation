import pytest
from methods.Get import Get
from test_data.TestData import Status, Reason, Others, Keys
from tests.test_base import TestBase

@pytest.mark.parametrize('fixture_conf', ['/posts?key=AIzaSyA9sQzsGZ_C35C0crbzH8Dx3zQdg7hzcZo'], indirect=True)
class TestGetBlogs(TestBase):
    def test_status_code(self):
        assert Get(self.res).get_status_code() == Status().code_200

    def test_reason(self):
        assert Get(self.res).reason() == Reason().ok

