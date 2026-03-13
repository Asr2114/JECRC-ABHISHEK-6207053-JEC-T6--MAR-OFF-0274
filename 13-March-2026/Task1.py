from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

time.sleep(3)

search_bar = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")

logo = driver.find_element(By.CSS_SELECTOR, "#nav-logo-sprites")

cart = driver.find_element(By.CSS_SELECTOR, "#nav-cart")

signin = driver.find_element(By.CSS_SELECTOR, "#nav-tools a")

categories = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")

print("Total category links:", len(categories))

time.sleep(3)

driver.quit()