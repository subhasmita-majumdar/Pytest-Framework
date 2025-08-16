import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCrossBrowserTest:
    @pytest.fixture(params=["chrome","firefox"],scope="class",autouse=True)
    def initialiseBrowser(self,request):
        global driver
        if request.param=='chrome':
            driver=webdriver.Chrome()
        elif request.param=='firefox':
            driver=webdriver.Firefox()
        request.cls.driver=driver

        yield
        driver.delete_all_cookies()
        driver.close()

    def test_launchURL(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()
        assert self.driver.title.__eq__("Test Login | Practice Test Automation")

    def test_loginApp(self):
        self.driver.find_element(By.ID,"username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("Password123")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.title.__eq__("Logged In Successfully | Practice Test Automation")

    def test_MenuItemsNavigation(self):
        menuItemList = self.driver.find_elements(By.CSS_SELECTOR, "#menu-primary-items li")
        expected_menu_list=["HOME","PRACTICE","COURSES","BLOG","CONTACT"]
        actual_menu_list=[]
        for eachItem in menuItemList:
            actual_menu_list.append(eachItem.text)
        print("Expected Menu List:{} and Actual Menu List:{}".format(expected_menu_list,actual_menu_list))
        assert expected_menu_list.__eq__(actual_menu_list)

    def test_logoutApp(self):
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        assert self.driver.title.__eq__("Test Login | Practice Test Automation")

