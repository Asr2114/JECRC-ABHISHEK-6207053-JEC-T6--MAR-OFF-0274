from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

price = driver.find_element(
    By.XPATH, "//table[@name='BookTable']//tr[td[text()='Learn Java']]/td[4]"
).text

print("Price of Learn Java: ", price)

time.sleep(2)