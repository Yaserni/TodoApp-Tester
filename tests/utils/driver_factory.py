from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from utils.custom_driver_downloader import ensure_chromedriver


def get_selenium_driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver_path = ensure_chromedriver()
    service = Service(executable_path=driver_path)
    return webdriver.Chrome(service=service, options=options)
