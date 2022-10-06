from time import sleep

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage


class TestCreateAcc:
    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions

        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        sleep(7)
        # Steps
        yield StartPage(driver)
        # Post-conditions
        driver.close()
        sleep(7)

    def test_open_create_acc(self, start_page):
        create_acc_page = start_page.navigate_to_create_acc()
        print(create_acc_page)
