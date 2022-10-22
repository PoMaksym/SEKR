from constants.create_acc_page import CreateAccountConsts
from pages.base_page import BasePage
from pages.utils import log_decorator


class CreateAccPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreateAccountConsts()

    @log_decorator
    def verify_open_create_page(self):
        """Verify create account page opened"""
        assert self.get_element_text(self.constants.VERIFY_CREATE_ACC_XPATH)

    @log_decorator
    def sign_up_with_email(self, user):
        """Sign up with email"""
        # Select Sign up with email
        self.click(xpath=self.constants.SIGN_UP_WITH_EMAIL_XPATH)
        # Fill fields
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_PLACEHOLDER, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_PLACEHOLDER, value=user.password)
        # Click button
        self.click(xpath=self.constants.CREATE_ACC_BUTTON_XPATH)
        # Select code
        self.click(xpath=self.constants.SIGN_UP_CODE_XPATH)
        self.click(self.constants.CODE_SELECTION_XPATH.format(option=self.constants.OPTION_MX_TEXT))
        # Fill phone number
        self.fill_field(self.constants.ENTER_PHONE_NUM_XPATH, value="380504520286")
        # Click Send me link
        self.click(xpath=self.constants.SEND_LINK_XPATH)
        # Verify success sign up.
        assert self.get_element_text(self.constants.SUCCESSFUL_SIGN_UP_XPATH) == self.constants.VERIFY_SUCCESSFUL_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESSFUL_SIGN_UP_XPATH)}"

    @log_decorator
    def verify_used_email(self, user):
        """Verify used email"""
        self.click(xpath=self.constants.SIGN_UP_WITH_EMAIL_XPATH)
        # Fill fields
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_PLACEHOLDER, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_PLACEHOLDER, value=user.password)
        # Click button
        self.click(xpath=self.constants.CREATE_ACC_BUTTON_XPATH)
        assert self.get_element_text(
            self.constants.SIGN_UP_EMAIL_USED_XPATH) == self.constants.SIGN_UP_EMAIL_USED_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SIGN_UP_EMAIL_USED_XPATH)}"

    @log_decorator
    def verify_invalid_password(self, user):
        """Verify invalid password"""
        self.click(xpath=self.constants.SIGN_UP_WITH_EMAIL_XPATH)
        # Fill fields
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_PLACEHOLDER, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_PLACEHOLDER, value=user.password)
        # Click button
        self.click(xpath=self.constants.CREATE_ACC_BUTTON_XPATH)
        assert self.get_element_text(
            self.constants.PASSWORD_LESS_SYMBOL_XPATH) == self.constants.PASSWORD_LESS_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.PASSWORD_LESS_SYMBOL_XPATH)}"

    @log_decorator
    def verify_empty_email_field(self, user):
        """Verify empty email field"""
        self.click(xpath=self.constants.SIGN_UP_WITH_EMAIL_XPATH)
        # Fill fields
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_PLACEHOLDER, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_PLACEHOLDER, value=user.password)
        # Click button
        self.click(xpath=self.constants.CREATE_ACC_BUTTON_XPATH)
        assert self.get_element_text(
            self.constants.EMPTY_EMAIL_SIGNUP_XPATH) == self.constants.EMPTY_EMAIL_SIGNUP_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.EMPTY_EMAIL_SIGNUP_XPATH)}"
