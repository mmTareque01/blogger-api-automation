import pytest
from methods.Get import Get
from test_data.TestData import Status, Reason, Others, Keys
from tests.test_base import TestBasePost


class TestAddNewPost(TestBasePost):

    def test_status_code(self):
        assert Get(self.res).get_status_code() == Status().code_200

    def test_reason(self):
        assert Get(self.res).reason() == Reason().ok

    def test_content_type(self):
        assert Others().content_type in Get(self.res).content_type()

    def test_blogs_title(self):
        assert Get(self.res).verify_properties("title")[0] == 'A new post'

    def test_author_name(self):
        assert Get(self.res).verify_properties("author.displayName")[0] == 'Muhimenul Tareque'

    def test_url(self):
        assert len(Get(self.res).verify_properties("url")) > 0

    def test_etag(self):
        assert len(Get(self.res).verify_properties("etag")) >0


