from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(3)

print("Title:", driver.title)

username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)

print("Current URL:", driver.current_url)

if "dashboard" in driver.current_url.lower():
    print("successful login")

driver.quit()