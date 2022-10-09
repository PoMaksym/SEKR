from time import sleep

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


@pytest.fixture()
def start_page():
    # Pre-conditions
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(1)
    sleep(5)
    # Steps
    yield StartPage(driver)
    # Post-conditions
    driver.close()


@pytest.fixture()
def sign_up_value():
    user = User()
    user.sign_up_value()
    return user
