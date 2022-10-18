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
    driver.implicitly_wait(20)
    # Steps
    yield StartPage(driver)
    # Post-conditions
    driver.close()


@pytest.fixture()
def sign_up_value():
    user = User()
    user.sign_up_value()
    return user


@pytest.fixture(scope="function")
def subscribe_fix():
    user = User()
    user.subscribe_value()
    return user


@pytest.fixture()
def contact_us():
    form = User()
    form.contact_us_value()
    return form
