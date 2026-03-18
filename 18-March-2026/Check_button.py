from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com")
driver.maximize_window()

time.sleep(3)

pincode = driver.find_element(By.XPATH, "//div[contains(text(),'Enter pincode')]")
pincode.send_keys("302012")

time.sleep(3)

check_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Check')]")


print("Is Check Button Enabled:", check_btn.is_enabled())
driver.quit()