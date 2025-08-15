import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestRaiseException:
    @pytest.fixture(scope="class",autouse=True)
    def setUp(self,request):
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        request.cls.driver=driver

        yield
        driver.delete_all_cookies()
        driver.close()

    def test_login(self):
        pytest.raises(NoSuchElementException)
        self.driver.find_element(By.ID,"username1").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("student")
        self.driver.find_element(By.ID, "submit").click()