import pytest
from selene import browser

@pytest.fixture(autouse=True)
def quit_browser():
    yield browser.quit()