import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import *

@pytest.fixture(scope="session")
def login():
    driver_path = "cases/chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()