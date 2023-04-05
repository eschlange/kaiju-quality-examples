"""
Base main utility functions
"""
from enum import Enum

from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, WebDriverException)
from selenium.webdriver.common.by import By

DEFAULT_TIME_DELAY = 10

# TODO: SPLIT THESE UP INTO DIFFERENT .py FILES - malexander 4/5/2023


class Elements:

    def __init__(self, element_type="", element="", descriptor=""):
        self.element_type = element_type.value
        self.element = element
        self.descriptor = descriptor


class ElementType(Enum):
    ID = By.ID
    NAME = By.NAME
    XPATH = By.XPATH
    CLASS = By.CLASS_NAME
    CSS = By.CSS_SELECTOR


class Finders:
    """
    Class to handle methods to find/wait for objects
    """

    def __int__(self, driver):
        self.driver = driver

    @staticmethod
    def find_element(driver, element):
        found_element = None
        try:
            found_element = driver.find_element(element.element_type, element.element)
        except (StaleElementReferenceException, NoSuchElementException) as err:
            print("Error! Element not found: {0} | {1}".format(element.element_type, err))
            raise WebDriverException("This test was terminated. Follow the stack for more information.")
        print("'{0}' element found".format(element.descriptor))
        return found_element


class Interact:
    """
    Class to interact with website
    """
    def __int__(self, driver):
        self.driver = driver

    @staticmethod
    def input_text(driver, element, input_text):
        found_element = Finders.find_element(driver, element)
        found_element.send_keys(input_text)
        print("Input text: test pyramid")

    @staticmethod
    def click_element(driver, element):
        found_element = Finders.find_element(driver, element)
        print("Click: {0}".format(element.descriptor))
        found_element.click()

    @staticmethod
    def get_text(driver, element):
        found_element = Finders.find_element(driver, element)
        print("Get text for: {0}".format(element.descriptor))
        return found_element.text


class BrowserSettings:
    """
    Class to handle Browser Settings
    """

    @staticmethod
    def set_browser(browser=""):
        try:
            if browser.lower() == "chrome":
                driver = webdriver.Chrome()
                driver.maximize_window()
            elif browser.lower() == "firefox":
                driver = webdriver.Firefox()
            elif browser.lower() == "edge":
                driver = webdriver.Edge()
            driver.maximize_window()
        except UnboundLocalError as err:
            print("You selected an invalid Webdriver name. Please ensure you provided the correct information.")
            print("Error: {0}".format(err))
        return driver

    @staticmethod
    def navigate_to_url(driver, url):
        driver.get(url)
