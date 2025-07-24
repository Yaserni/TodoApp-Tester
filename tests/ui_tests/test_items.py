from pages.item_list_page import ItemListPage
from pages.login_page import LoginPage


class TestItems:

    def login_and_go_to_items(self, driver):
        login = LoginPage(driver)
        login.load()
        login.login("admin", "1234")

    def test_add_item(self, driver):
        self.login_and_go_to_items(driver)
        items = ItemListPage(driver)
        items.add_item("Buy Milk")
        assert items.item_exists("Buy Milk")

    def test_edit_item(self, driver):
        self.login_and_go_to_items(driver)
        items = ItemListPage(driver)
        items.edit_item("Buy Milk", "Buy Bread")
        assert items.item_exists("Buy Bread")

    def test_delete_item(self, driver):
        self.login_and_go_to_items(driver)
        items = ItemListPage(driver)
        items.delete_item("Buy Bread")
        assert not items.item_exists("Buy Bread")
