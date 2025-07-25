import time

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.CSS_SELECTOR, 'input[placeholder="Username"]')
        self.password_input = (By.CSS_SELECTOR, 'input[placeholder="Password"]')
        self.login_button = (By.XPATH, '//button[text()="Login"]')
        self.error_text = (By.CLASS_NAME, 'error')

    def load(self):
        self.driver.get("http://localhost:3000")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)

    def get_error_message(self):
        return self.driver.find_element(*self.error_text).text
