import unittest
import pytest
from selenium import webdriver
from pages.home.webshop_page import WebshopPage


class TestLogin(unittest.TestCase):
    baseURL = "http://staging.togital.no/konkurrenten/webshop/#/reise/"
    driver = webdriver.Firefox()
    # driver.maximize_window() #Find a solution for the maximize window issue
    driver.get(baseURL)
    driver.implicitly_wait(3)
    wp = WebshopPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        # Login with the given valid credentials
        self.wp.login("istvan.kisgyorgy@redrock.no", "1234")
        # Make sure that the login was successful by checking the presence of the 'Logout' button
        isLoginSuccessful = self.wp.verifyLoginSuccessful()
        assert isLoginSuccessful == True

    @pytest.mark.run(order=1)
    def test_invalidCredentialsLogin(self):
        # Login with the given invalid credentials
        self.wp.login("istvan.kisgyorgy@redrock.no", "123456")
        # Make sure that the login was unsuccessful by checking the thrown error message
        isLoginUnsuccessful = self.wp.verifyLoginUnsuccessful()
        assert isLoginUnsuccessful == True