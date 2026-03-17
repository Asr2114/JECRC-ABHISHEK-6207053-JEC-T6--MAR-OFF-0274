from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)

browsers = driver.find_elements(By.XPATH, "//table[@id='taskTable']//tr/td[1]")

for browser in browsers:
    print(browser.text)

time.sleep(2)
driver.quit()