from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/main/div/div/div/div[2]/div[1]/input").send_keys("Abhishek")
time.sleep(1)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/main/div/div/div/div[2]/div[2]/input").send_keys("test@gmail.com")
time.sleep(1)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/main/div/div/div/div[2]/div[3]/input").send_keys("9999999999")

time.sleep(3)

driver.quit()