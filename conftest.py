import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage


@pytest.fixture(scope="function")
def start_page():
    # Pre-conditions

    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BASE_URL)
    driver.implicitly_wait(1)
    # Steps
    yield StartPage(driver)
    # Post-conditions
    driver.close()
