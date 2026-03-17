from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
time.sleep(2)

element = driver.find_element(By.PARTIAL_LINK_TEXT, "Mobiles")

print(element.text)

time.sleep(2)

driver.quit()
