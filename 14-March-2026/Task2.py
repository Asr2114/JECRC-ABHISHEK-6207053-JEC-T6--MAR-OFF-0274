from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()



time.sleep(3)


subject = driver.find_element(
    By.XPATH, "//td[text()='Amod']/ancestor::tr/preceding-sibling::tr[1]/td[3]"
).text

print("Subject: ", subject)
time.sleep(2)

driver.quit()

