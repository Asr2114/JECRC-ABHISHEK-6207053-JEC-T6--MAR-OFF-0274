from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

time.sleep(2)

element = driver.find_element(By.XPATH, "//a[contains(text(),'Mobiles')]/preceding-sibling::a[1]")
print(element.text)

time.sleep(3)

driver.quit()
