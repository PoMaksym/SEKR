from constants.start_page import StartPageConsts
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_decorator



class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConsts()

    @wait_until_ok(timeout=5, period=1)
    @log_decorator
    def subscribe_fill_fields(self, user):
        """Sign up on Subscribe"""
        # Fill fields
        self.fill_field(xpath=self.constants.SUBSCRIBE_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SUBSCRIBE_NAME_XPATH, value=user.name)
        self.fill_field(xpath=self.constants.SUBSCRIBE_SURNAME_XPATH, value=user.surname)
        # Click button Sign Up
        self.click(xpath=self.constants.SUBSCRIBE_SIGNUP_XPATH)

    @log_decorator
    def verify_subscribe(self):
        """Verify subscribe"""
        assert self.get_element_text(self.constants.SUBSCRIBE_VERIFY_XPATH) == self.constants.SUBSCRIBE_VERIFY_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SUBSCRIBE_VERIFY_XPATH)}"

    @log_decorator
    def navigate_to_create_acc(self):
        """Open create an account page"""
        self.click(self.constants.CREATE_ACC_HOMEPAGE_XPATH)
        from pages.create_acc_page import CreateAccPage
        return CreateAccPage(self.driver)
