import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()
