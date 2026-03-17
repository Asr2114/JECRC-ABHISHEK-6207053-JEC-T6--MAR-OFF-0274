from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

time.sleep(3)

search = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
print("Search bar found")

logo = driver.find_element(By.CSS_SELECTOR, "#nav-logo-sprites")
print("Logo found")

cart = driver.find_element(By.CSS_SELECTOR, "#nav-cart")
print("Cart found")

signin = driver.find_element(By.CSS_SELECTOR, "#nav-tools a")
print("Sign in found")

categories = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")
print("Total categories:", len(categories))

time.sleep(3)
driver.quit()