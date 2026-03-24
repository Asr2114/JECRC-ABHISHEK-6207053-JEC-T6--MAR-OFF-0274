from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.myntra.com/")
driver.maximize_window()
time.sleep(2)

action = ActionChains(driver)

men = driver.find_element(By.XPATH, "//a[text()='Men']")
action.move_to_element(men).perform()

time.sleep(3)

ele = driver.find_element(By.XPATH, "//a[text()='Sweatshirts']")
ele.click()
time.sleep(2)


action.scroll_by_amount(0, 1500).perform()
time.sleep(4)
driver.quit()