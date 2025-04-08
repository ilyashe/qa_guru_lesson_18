import pytest
from selene import browser

from api.api_session import TestSession


@pytest.fixture()
def api_session():
    session = TestSession(base_url='https://demowebshop.tricentis.com/')
    return session

@pytest.fixture(autouse=True)
def quit_browser():
    yield browser.quit()