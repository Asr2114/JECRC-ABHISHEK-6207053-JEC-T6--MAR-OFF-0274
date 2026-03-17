from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")
driver.maximize_window()

time.sleep(3)

print("Title:", driver.title)

yes_radio = driver.find_element(By.XPATH, "//label[text()='Yes']")
yes_radio.click()

time.sleep(2)

result = driver.find_element(By.CLASS_NAME, "text-success")
print("Result:", result.text)

print("Class:", yes_radio.get_attribute("class"))
print("ID:", yes_radio.get_attribute("id"))

print("Current URL:", driver.current_url)

driver.quit()