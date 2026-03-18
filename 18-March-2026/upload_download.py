from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize()

choose_file = driver.find_element(By.ID, "file-upload")

choose_file.send_keys("/Users/asr2114/Downloads/For my Loveeee.png")

submit_button = driver.find_element(By.ID, "file-submit")

submit_button.click()

time.sleep(2)



driver.get("https://the-internet.herokuapp.com/download/")

driver.maximize_window()
driver.find_element(By.XPATH, "For my Loveeee.png")