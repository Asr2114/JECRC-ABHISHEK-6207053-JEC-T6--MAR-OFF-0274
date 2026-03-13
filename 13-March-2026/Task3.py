from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)

driver.find_element(By.XPATH, '//a[text()="Home"]').click()

time.sleep(2)

driver.quit()

