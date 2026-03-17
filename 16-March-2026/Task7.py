from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

time.sleep(2)

username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password = driver.find_element(By.CSS_SELECTOR, "input#password")
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
footer = driver.find_element(By.CSS_SELECTOR, "#page-footer a")

print("All elements located successfully")

time.sleep(3)
driver.quit()