from time import sleep

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User, log_decorator


class TestCreateAcc:

    @pytest.fixture()
    def start_page(self):
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
    def sign_up_value(self):
        user = User()
        user.sign_up_value()
        return user

    @log_decorator
    def test_sign_up_with_email(self, start_page, sign_up_value):
        """Steps:
         - Open create an account page
         - sign up with email
         - Fill fields with valid data"""
        # create_acc_page = start_page
        # Open create an account
        create_acc_page = start_page.navigate_to_create_acc()
        # Verify page opened
        create_acc_page.verify_open_create_page()
        # Fill fields email and password
        user = sign_up_value
        create_acc_page.sign_up_with_email(user)

    def test_sign_up_used_email(self, start_page, sign_up_value):
        """Steps:
            - Open create an account page
            - sign up with email
            - Fill email field with used email"""
        user = sign_up_value
        user.email = 'maksym.po@room4.team'
        create_acc_page = start_page.navigate_to_create_acc()
        create_acc_page.verify_used_email(user)

    def test_sign_up_via_goo(self, start_page):
        create_acc_page = start_page.navigate_to_create_acc()
        create_acc_page.sign_up_goo()
