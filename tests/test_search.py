import pytest
from methods.Get import Get
from test_data.TestData import Status, Reason, Others, Keys
from tests.test_base import TestBase

@pytest.mark.parametrize('fixture_conf', ['/posts/search?q=dummy&key=AIzaSyA9sQzsGZ_C35C0crbzH8Dx3zQdg7hzcZo'], indirect=True)
class TestSearch(TestBase):
    def test_status_code(self):
        assert Get(self.res).get_status_code() == Status().code_200

    def test_reason(self):
        assert Get(self.res).reason() == Reason().ok

    def test_content_type(self):
        assert Others().content_type in Get(self.res).content_type()

    def test_blogs_length(self):
        assert 0 <= len(Get(self.res).verify_properties(Keys().items)) <= 10

    def test_etag(self):
        assert len(Get(self.res).verify_properties("etag")) >0


