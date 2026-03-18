from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

dropdown = Select(driver.find_element(By.ID, "country"))


# dropdown = Select(country_dropdown)

dropdown.select_by_value('usa')


time.sleep(2)

dropdown.select_by_index(3)

time.sleep(2)

dropdown.select_by_visible_text('Japan')

driver.quit()






