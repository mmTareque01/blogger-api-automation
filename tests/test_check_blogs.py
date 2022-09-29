import pytest
from methods.Get import Get
from test_data.TestData import Status, Reason, Others, Keys
from tests.test_base import TestBase

@pytest.mark.parametrize('fixture_conf', ['?key=AIzaSyA9sQzsGZ_C35C0crbzH8Dx3zQdg7hzcZo'], indirect=True)
class TestCheckBlogs(TestBase):
    def test_status_code(self):
        assert Get(self.res).get_status_code() == Status().code_200

    def test_reason(self):
        assert Get(self.res).reason() == Reason().ok

    def test_content_type(self):
        assert Others().content_type in Get(self.res).content_type()

    def test_total_blogs(self):
        assert Get(self.res).verify_properties("posts.totalItems")[0] == Others().total_blogs

    def test_total_page(self):
        assert Get(self.res).verify_properties("pages.totalItems")[0] == Others().total_page

    def test_blog_name(self):
        assert Get(self.res).verify_properties("name")[0] == Others().name

    def test_blog_id(self):
        assert int(Get(self.res).verify_properties("id")[0]) == Others().id

    def test_blog_language(self):
        assert Get(self.res).verify_properties("locale.language")[0] == Others().language
