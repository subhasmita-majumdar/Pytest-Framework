from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

@pytest.mark.order(2)
def test_LoginSuccessMessage():
    success_flag = driver.find_element(By.CLASS_NAME, "post-title").is_displayed()
    assert success_flag, "Success message not found"
    login_success_msg = driver.find_element(By.CLASS_NAME, "post-title").text
    print(login_success_msg)

@pytest.mark.order(3)
def test_Logout():
    driver.find_element(By.LINK_TEXT, "Log out").click()
    expected_title = "Test Login | Practice Test Automation"
    actual_title = driver.title
    assert actual_title.__eq__(expected_title)
    driver.close()

@pytest.mark.order(1)
def test_login():
    driver.find_element(By.ID, "username").send_keys('student')
    driver.find_element(By.ID, "password").send_keys('Password123')
    driver.find_element(By.ID, "submit").click()
    expected_title = "Logged In Successfully | Practice Test Automation"
    actual_title = driver.title
    assert actual_title.__eq__(expected_title)



