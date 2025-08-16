import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPytestOrder:
    driver = webdriver.Chrome()

    @pytest.fixture(scope="class",autouse=True)
    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()

        yield
        self.driver.delete_all_cookies()
        self.driver.close()

    @pytest.mark.login
    def test_Login(self):
        self.driver.find_element(By.ID, "username").send_keys('student')
        self.driver.find_element(By.ID, "password").send_keys('Password123')
        self.driver.find_element(By.ID, "submit").click()
        print(self.driver.title)

    @pytest.mark.title
    def test_HomePageTitle(self):
        expected_title = "Logged In Successfully | Practice Test Automation"
        actual_title = self.driver.title
        assert actual_title.__eq__(expected_title)
        print("Log In Success")

    @pytest.mark.login
    def test_LoginSuccessMessage(self):
        success_flag = self.driver.find_element(By.CLASS_NAME,"post-title").is_displayed()
        assert success_flag,"Success message not found"
        login_success_msg=self.driver.find_element(By.CLASS_NAME,"post-title").text
        print(login_success_msg)

    @pytest.mark.login
    def test_LogoutButtonPresence(self):
        logout_button_flag = self.driver.find_element(By.LINK_TEXT, "Log out").is_displayed()
        assert logout_button_flag, "Success message not found"
        print("Log out button found")

