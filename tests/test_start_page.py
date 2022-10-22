class TestStartPage:

    def test_subscribe(self, start_page, subscribe_fix):
        """Pre-conditions:
        - open website
        - fill fields (email, name, surname)
        - verify message"""
        user = subscribe_fix
        # Fill fields with random data
        start_page.subscribe_fill_fields(user)
        # Verify Subscribe successfuly
        start_page.verify_subscribe()
