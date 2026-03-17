from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)

books = driver.find_elements(By.XPATH, "//td[text()='300']/ancestor::tr/td[1]")

for book in books:
    print("Book Name:", book.text)

time.sleep(2)
driver.quit()