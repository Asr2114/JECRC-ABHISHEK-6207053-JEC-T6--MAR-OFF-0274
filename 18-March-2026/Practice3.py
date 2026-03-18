from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.lenskart.com/sunglasses.html")

driver.maximize_window()
time.sleep(2)

dropdown = Select(driver.find_element(By.ID, 'sortByDropdown'))

dropdown.select_by_index(1)
time.sleep(2)

# product = driver.find_element(By.XPATH, "(//div[contains(@id,'209536')])")
product = driver.find_element(By.ID, '152554')

print(product.text)


driver.quit()
