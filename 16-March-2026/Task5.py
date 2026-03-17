from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

time.sleep(2)

username = driver.find_element(By.XPATH, "//input[@name='username']")
print("Username located")

password = driver.find_element(By.XPATH, "//input[@id='password']")
print("Password located")

login = driver.find_element(By.XPATH, "//button[@type='submit']")
print("Login button located")

elemental = driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']")
print("Elemental Selenium link located")

heading = driver.find_element(By.XPATH, "//h2[contains(text(),'Login Page')]")
print("Heading located")

time.sleep(3)
driver.quit()