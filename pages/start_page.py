from time import sleep

from constants.start_page import StartPageConsts
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConsts()

    def subscribe_fill_fields(self, user):
        """Sign up on Subscribe"""
        # Fill fields
        self.fill_field(xpath=self.constants.SUBSCRIBE_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SUBSCRIBE_NAME_XPATH, value=user.name)
        self.fill_field(xpath=self.constants.SUBSCRIBE_SURNAME_XPATH, value=user.surname)
        sleep(5)
        # Click button
        self.click(xpath=self.constants.SUBSCRIBE_SIGNUP_XPATH)
        # return StartPage(self.driver)

    def verify_subscribe(self):
        """Verify subscribe"""

        assert self.get_element_text(self.constants.SUBSCRIBE_VERIFY_XPATH) == self.constants.SUBSCRIBE_VERIFY_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SUBSCRIBE_VERIFY_XPATH)}"

    def navigate_to_create_acc(self):
        self.click(self.constants.CREATE_ACC_HOMEPAGE_XPATH)
