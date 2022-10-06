from time import sleep

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


class TestStartPage:

    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions

        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.maximize_window()
        driver.implicitly_wait(1)
        sleep(5)
        # # Steps
        yield StartPage(driver)
        # Post-conditions
        driver.close()

    @pytest.fixture(scope="function")
    def subscribe_fix(self):
        user = User()
        user.subscribe_value()
        return user

    def test_subscribe(self, start_page, subscribe_fix):
        """Pre-conditions:
        - open website
        - fill fields (email, name, surname)
        - verify message"""
        user = subscribe_fix
        start_page.subscribe_fill_fields(user)
        sleep(5)
        start_page.verify_subscribe()

    def test_open_create_acc_page(self, start_page):
        create_acc_page = start_page
        start_page.navigate_to_create_acc()
        print(create_acc_page)
        sleep(5)
