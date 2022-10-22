from pages.utils import User


class TestCreateAcc:

    def test_sign_up_with_email(self, start_page, sign_up_value):
        """Steps:
         - Open create an account page
         - sign up with email
         - Fill fields with valid data"""
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
        # Open create account page
        create_acc_page = start_page.navigate_to_create_acc()
        # Fill email field with used email
        user = sign_up_value
        user.email = 'maksym.po@room4.team'
        # Verify sign up with used email
        create_acc_page.verify_used_email(user)

    def test_sign_up_empty_field(self, start_page, sign_up_value):
        """Verify empty email field"""
        # Open create account page
        create_acc_page = start_page.navigate_to_create_acc()
        # Leave fields empty
        user = User()
        # Verify Sign Up with empty fields
        create_acc_page.verify_empty_email_field(user)

    def test_wrong_password(self, start_page, sign_up_value):
        """Steps:
        - Open create an account page
        - sign up with email
        - Fill password field with 1 symbols"""
        # Open create account page
        create_acc_page = start_page.navigate_to_create_acc()
        user = sign_up_value
        user.password = '1'
        # Verify wrong password
        create_acc_page.verify_invalid_password(user)
