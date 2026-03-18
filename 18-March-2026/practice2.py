from selenium import webdriver
from selenium.webdriver.common.by import By
import time


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.lenskart.com/")
driver.maximize_window()

time.sleep(5)

eye= driver.find_element(By.ID, 'lrd1')
# print(eye.text)

assert 'GLASSES' == eye.text, "didnt find"

print('Success')



driver.quit()