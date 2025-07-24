import pytest

from utils.driver_factory import get_selenium_driver


@pytest.fixture
def driver(request):
    self = request.cls
    self.driver = get_selenium_driver()
    yield self.driver
    self.driver.quit()
