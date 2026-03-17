from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

time.sleep(2)

# ID
search = driver.find_element(By.ID, "searchInput")
print("ID locator found")

# Name
search_name = driver.find_element(By.NAME, "search")
print("Name locator found")

# Class Name
logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
print("Class Name locator found")

# Tag Name
inputs = driver.find_elements(By.TAG_NAME, "input")
print("Tag Name count:", len(inputs))

# CSS Selector
english = driver.find_element(By.CSS_SELECTOR, "#js-link-box-en")
print("CSS Selector found")

# XPath
heading = driver.find_element(By.XPATH, "//strong")
print("XPath locator found")

time.sleep(3)
driver.quit()