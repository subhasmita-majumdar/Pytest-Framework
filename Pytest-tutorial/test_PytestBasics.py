import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_module():
    global driver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)

class TestPytestBasics:
    @staticmethod
    def setup_class():
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()

    @staticmethod
    def setup_method():
        driver.find_element(By.ID,"username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

    def test_VerifyTitle(self):
        expected_title="Logged In Successfully | Practice Test Automation"
        actual_title=driver.title
        assert actual_title.__eq__(expected_title)

    def test_VerifyHomePageURL(self):
        expected_url="https://practicetestautomation.com/logged-in-successfully/"
        actual_url=driver.current_url
        assert actual_url.__eq__(expected_url)

    @staticmethod
    def teardown_method():
        driver.find_element(By.LINK_TEXT,"Log out").click()

    @staticmethod
    def teardown_class():
        driver.delete_all_cookies()

def teardown_module():
    driver.close()

