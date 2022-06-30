import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="None",
                     help="Choose language: en-gb, ru, fr, de, es, it, sk, pt")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language in ("en-gb", "ru", "fr", "de", "es", "it", "sk", "pt"):
        print("\nstart chrome browser for test language = " + user_language)
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be en, ru, es")
    yield browser
    print("\nquit browser..")
    browser.quit()

#pytest --language=es test_items.py
