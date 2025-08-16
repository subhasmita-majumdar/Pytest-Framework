import time

import pytest
from selenium.webdriver.common.by import By


class TestLoginFailure:
    @pytest.mark.parametrize("username,password", [("student", "Password123")])
    def test_validLogin(self, setUp, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.title.__eq__("Logged In Successfully | Practice Test Automation")
        self.driver.find_element(By.LINK_TEXT, "Log out").click()

    @pytest.mark.parametrize(
                                "username,password",
                                [
                                    ("incorrectUser","Password123"),
                                    ("student","incorrectPassword")
                                ]
                            )
    def test_invalidLogin(self,setUp,username,password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        error_message_display_flag = self.driver.find_element(By.ID,"error").is_displayed()
        assert error_message_display_flag.__eq__(True)

