from time import sleep

import pytest

from pages.utils import User


class TestStartPage:

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
