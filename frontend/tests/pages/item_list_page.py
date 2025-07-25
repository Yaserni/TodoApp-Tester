import time

from selenium.webdriver.common.by import By


class ItemListPage:
    def __init__(self, driver):
        self.driver = driver
        self.new_item_input = (By.CSS_SELECTOR, 'input[placeholder="Add new item"]')
        self.add_button = (By.XPATH, '//button[text()="Add"]')

    def add_item(self, name):
        self.driver.find_element(*self.new_item_input).send_keys(name)
        self.driver.find_element(*self.add_button).click()

    def edit_item(self, old_name, new_name):
        item = self.driver.find_element(By.XPATH, f"//li[contains(.,'{old_name}')]")
        edit_btn = item.find_element(By.XPATH, ".//button[contains(text(),'Edit')]")
        edit_btn.click()
        input_field = item.find_element(By.TAG_NAME, 'input')
        input_field.clear()
        input_field.send_keys(new_name)
        save_btn = item.find_element(By.XPATH, ".//button[contains(text(),'Save')]")
        save_btn.click()

    def delete_item(self, name):
        item = self.driver.find_element(By.XPATH, f"//li[contains(.,'{name}')]")
        delete_btn = item.find_element(By.XPATH, ".//button[contains(text(),'Delete')]")
        delete_btn.click()

    def item_exists(self, name):
        time.sleep(1)
        return name in self.driver.page_source
