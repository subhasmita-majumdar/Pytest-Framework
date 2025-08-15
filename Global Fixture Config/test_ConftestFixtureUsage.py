import pytest
from selenium.webdriver.common.by import By

class TestConftestFixtureUsage:
    def test_MenuItemsNavigation(self,setUp):
        menuItemList = self.driver.find_elements(By.CSS_SELECTOR, "#menu-primary-items li")
        expected_menu_list=["HOME","PRACTICE","COURSES","BLOG","CONTACT"]
        actual_menu_list=[]
        for eachItem in menuItemList:
            actual_menu_list.append(eachItem.text)
        print("Expected Menu List:{} and Actual Menu List:{}".format(expected_menu_list,actual_menu_list))
        assert expected_menu_list.__eq__(actual_menu_list)