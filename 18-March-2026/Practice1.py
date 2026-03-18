from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")
driver.maximize_window()

time.sleep(3)

yes_radio = driver.find_element(By.XPATH, "//label[text() = 'Yes']")

print("Is Displayed:", yes_radio.is_displayed())
print("Is Enabled:", yes_radio.is_enabled())

yes_radio.click()
time.sleep(2)

radio_input = driver.find_element(By.ID, "yesRadio")
print("Is Selected:", radio_input.is_selected())