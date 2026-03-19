from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time




driver = webdriver.Chrome()
driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("Abhishek")
driver.find_element(By.ID, "email").send_keys("test@gmail.com")

driver.find_element(By.ID, "tel").send_keys("09092090290239029029302")








# wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Male']"))).click()

driver.find_element(By.XPATH, "//input[@value='three']").click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='automationtesting']"))).click()
#
# driver.find_element(By.XPATH, "//input[@value='selenium']").click()








wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()

time.sleep(5)


driver.quit()
