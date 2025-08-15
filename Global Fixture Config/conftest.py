import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(params=['chrome','firefox'],scope="class")
def setUp(request):
    global driver
    if request.param=='chrome':
        driver=webdriver.Chrome()
    elif request.param=='firefox':
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    request.cls.driver=driver

    yield
    driver.delete_all_cookies()
    driver.close()