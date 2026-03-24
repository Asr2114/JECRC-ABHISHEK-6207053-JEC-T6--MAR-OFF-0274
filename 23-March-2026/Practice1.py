from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/droppable")

driver.maximize_window()
time.sleep(2)

action = ActionChains(driver)

origin = driver.find_element(By. ID, 'draggable')
destination = driver.find_element(By.ID, 'droppable')

action.drag_and_drop(origin, destination).perform()

time.sleep(3)

driver.quit()

