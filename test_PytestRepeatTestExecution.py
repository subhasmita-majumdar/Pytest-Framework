import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRepeatation:
    @pytest.fixture(scope="class",autouse=True)
    def setUp(self,request):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        request.cls.driver=driver

        yield
        driver.delete_all_cookies()
        driver.close()

    def test_MenuItemsList(self):
        menuItemList=self.driver.find_elements(By.CSS_SELECTOR,"#menu-primary-items li")
        for eachItem in menuItemList:
            print(eachItem.text,end="\t")
        print()