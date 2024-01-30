import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="Users\Vinch\Desktop\QA_automation\Lesson_19\chromedriver.exe")
    yield driver
    driver.quit()
