"""This is the MOST basic sample of using Webdriver to validate a page is hit.
Accesses selenium functions: get, find_element, send_keys, click, and find_element text
Uses basic assert to provide "Pass/Fail status. try/except False assert to fail correctly"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

driver.find_element(By.NAME, "q").send_keys("test pyramid")
print("Input text: test pyramid")
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
print("Click 'Google Search' button")

expected_text = "Images for test pyramids"
actual_text = driver.find_element(By.XPATH,
                                  "//*[@id='rso']/div[2]/div/div/div[2]/g-section-with-header/div[1]/title-with-lhs-icon/a/div[3]/h3").text

if expected_text == actual_text:
    print("Text matches! :)")
    print("{0} == {1}".format(expected_text, actual_text))
    assert True
else:
    try:
        assert False
    except AssertionError as err:
        print("Text did not match. :(")
        print("{0} != {1}".format(expected_text, actual_text))
