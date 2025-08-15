from pytest_dependency import depends
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

@pytest.mark.dependency(name="login")
def test_login():
    driver.find_element(By.ID, "username").send_keys('student')
    driver.find_element(By.ID, "password").send_keys('Password123')
    driver.find_element(By.ID, "submit").click()
    expected_title = "Logged In Successfully | Practice Test Automation"
    actual_title = driver.title
    assert actual_title.__eq__(expected_title)

def test_LoginSuccessMessage(request):
    depends(request,["login"])
    success_flag = driver.find_element(By.CLASS_NAME, "post-title").is_displayed()
    assert success_flag, "Success message not found"
    login_success_msg = driver.find_element(By.CLASS_NAME, "post-title").text
    print(login_success_msg)

def test_Logout(request):
    depends(request,["login"])
    driver.find_element(By.LINK_TEXT, "Log out").click()
    expected_title = "Test Login | Practice Test Automation"
    actual_title = driver.title
    assert actual_title.__eq__(expected_title)
    driver.close()
