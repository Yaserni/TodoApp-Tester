from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, driver):
        page = LoginPage(driver)
        page.load()
        page.login("admin", "1234")
        assert driver.title == "Items Page", f"Expected title 'Items Page' but got '{driver.title}'"

    def test_invalid_login(self, driver):
        page = LoginPage(driver)
        page.load()
        page.login("bad", "wrong")
        assert driver.title == "Login Page", f"Expected title 'Login Page' but got '{driver.title}'"
        assert page.get_error_message() == 'Invalid username or password', "Error the error message should be 'Invalid username or password'"
