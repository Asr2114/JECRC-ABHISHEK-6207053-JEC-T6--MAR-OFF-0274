from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(2)

ancestor_element = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']/ancestor::div")

print("Ancestor Tag: ", ancestor_element.tag_name)

time.sleep(3)
driver.quit()