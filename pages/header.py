from constants.header import HeaderConsts
from pages.base_page import BasePage


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConsts()

    def navigate_to_create_acc(self):
        self.click(self.constants.CREATE_ACC_HOMEPAGE_XPATH)
