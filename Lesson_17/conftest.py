import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="C:\chromedriver")
    yield driver
    driver.quit()