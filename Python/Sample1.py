from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")


driver.find_element(By.NAME, "q").send_keys("Butts")

time.sleep(5)