import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from search import DuckDuckGoSearchPage
from results import DuckDuckGoResultPage


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    driver = Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def test_basic_duckduckgo_search(browser):
    PHRASE = 'panda'
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    time.sleep(3)

    search_page.search(PHRASE)
    time.sleep(3)
    result_page = DuckDuckGoResultPage(browser)

    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
