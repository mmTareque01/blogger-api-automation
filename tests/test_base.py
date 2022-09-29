import pytest


@pytest.mark.usefixtures("fixture_conf")
class TestBase:
    pass


@pytest.mark.usefixtures("fixture_conf_post")
class TestBasePost:
    pass
