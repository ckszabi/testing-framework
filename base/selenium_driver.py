from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
# import time
# import os

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        """
        Accepts a locator type and returns the 'By.TYPE', e.g. 'By.ID', 'By.NAME'. etc.
        """
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        """
        Based on the given locator value and locator type finds the element and returns it
        Default locator type: 'ID'
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locator type: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        """
        Based on the given locator value and locator type finds the element and operates a click action on it
        Default locator type: 'ID'
        """
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked the element with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.info("Cannot click the element with locator: " + locator + " and locator type: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        """
        Based on the given locator value and locator type finds the element and operates a typing (send_keys) action on
        it
        Default locator type: 'ID'
        """
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            element.send_keys(data)
            self.log.info("Typed into the element with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.info("Cannot type into the element with locator: " + locator + " and locator type: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = self.getElement(locator, locatorType)
            # if locator:  # This means if locator is not empty
            #     element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        """
        INCLUDE DESCRIPTION
        """
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element
