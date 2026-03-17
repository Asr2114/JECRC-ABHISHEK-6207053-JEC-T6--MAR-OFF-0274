from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
time.sleep(2)

driver.get("https://www.cricbuzz.com/")
time.sleep(2)

driver.get("https://www.myntra.com")
time.sleep(2)


driver.quit()


