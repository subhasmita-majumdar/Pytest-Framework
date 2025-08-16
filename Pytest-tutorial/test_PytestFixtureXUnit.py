import pytest

def setup_module(self):
    print("setup and initialize driver")

class TestLoginPage:
    def setup_class(self):
        print("launch application")

    def setup_method(self):
        print("log into application")

    def test_AppUrl(self):
        print("Verify app url")

    def test_AppTitle(self):
        print("Verify app title")

    def teardown_method(self):
        print("log out of application")

    def teardown_class(self):
        print("delete browser cookies")

def teardown_module(self):
    print("close the driver and end session")
