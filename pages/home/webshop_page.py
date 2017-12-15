from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging

class WebshopPage(SeleniumDriver):

    # This is the custom logger instance
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Enumerate all page locators here

    _login_link = "//a[contains(text(), 'Logg inn')]"
    _email_field = "email"
    _password_field = "//input[@placeholder='Passord']"
    _login_button = "//button[contains(text(), 'Logg inn')]"
    _logout_button = "//a[contains(text(), 'Logg ut')]"
    _failed_to_login_message = "//p[contains(text(), 'Feil passord og/eller epost, vennligst prøv på nytt')]"

    #######################################################
    # Defining all actions on all elements in this section#
    #######################################################

    def clickLoginLink(self):
        """
        Operates a click action on the top 'Login' link button element
        """
        self.elementClick(self._login_link, locatorType="xpath")

    def typeIntoEmailField(self, email):
        """
        Enters value into the 'Email' input field element in the 'Login' popup
        """
        self.sendKeys(email, self._email_field,locatorType="name")

    def typeIntoPasswordField(self, password):
        """
        Enters value into the 'Password' input field element in the 'Login' popup
        """
        self.sendKeys(password, self._password_field, "xpath")

    def clickLoginButton(self):
        """
        Operates a click action on the top 'Login' link button element
        """
        self.elementClick(self._login_button, "xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.typeIntoEmailField(email)
        self.typeIntoPasswordField(password)
        time.sleep(2)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        """
        Verifies if the 'Logout' button is present after the login or not and returns a boolean 'True' or 'False'
        """
        result = self.isElementPresent(self._logout_button, locatorType="xpath")
        return result

    def verifyLoginUnsuccessful(self):
        """
        Verifies if the error message is thrown after entering invalid credentials
        """
        result = self.isElementPresent(self._failed_to_login_message, locatorType="xpath")
        return result