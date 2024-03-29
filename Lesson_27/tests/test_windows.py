import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Lesson_27.src.pages.page_windows import WindowPage
from Lesson_27.data_for_test import text_for_window_message as expected_text

@pytest.mark.usefixtures("firefox")
class TestWindows:
    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = WindowPage(driver=self.driver)
        self.page.open()

        # ������ �� ������ �� ������ �������� �� ����� test tab
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # # ���������� �� ������ ���� switch_to - ������� �� ������
        # # window - ������� ��� �������� � ���� ����� ���������
        # # self.driver.window_handles[0] - ������������� ��������� ��� ����
        # self.driver.switch_to.window(self.driver.window_handles[1])
        # self.driver.switch_to.window(self.driver.window_handles[0])
    # def test_tab(self):
    #     self.page.open_new_tab()
    #     new_tab = self.driver.window_handles[1]
    #     self.driver.switch_to.window(new_tab)
    #     text = self.driver.find_element(By.ID, "sampleHeading").text
    #     assert "This is a sample page" in text

    def test_window_message(self):
        self.page.open_window_message()
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        text = self.driver.find_element(By.TAG_NAME, "body").text
        assert expected_text == text