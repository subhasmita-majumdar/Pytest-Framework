import pytest
from pytest_dependency import depends
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPytestParallelTesting:
    @pytest.fixture(scope="class",autouse=True)
    def setUpAndLogin(self,request):
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        driver.find_element(By.ID, "username").send_keys('student')
        driver.find_element(By.ID, "password").send_keys('Password123')
        driver.find_element(By.ID, "submit").click()
        request.cls.driver = driver

        yield
        driver.find_element(By.LINK_TEXT, "Log out").click()
        driver.delete_all_cookies()
        driver.close()

    def test_HomePageTitle(self):
        expected_title = "Logged In Successfully | Practice Test Automation"
        actual_title = self.driver.title
        assert actual_title.__eq__(expected_title)
        print("Log In Success")

    def test_LoginSuccessMessage(self):
        success_flag = self.driver.find_element(By.CLASS_NAME,"post-title").is_displayed()
        assert success_flag,"Success message not found"
        login_success_msg=self.driver.find_element(By.CLASS_NAME,"post-title").text
        print(login_success_msg)

    def test_LogoutButtonPresence(self):
        logout_button_flag = self.driver.find_element(By.LINK_TEXT, "Log out").is_displayed()
        assert logout_button_flag, "Success message not found"
        print("Log out button found")