from constants.create_acc_page import CreateAccountConsts
from pages.base_page import BasePage


class CreateAccPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreateAccountConsts()
