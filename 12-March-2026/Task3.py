#top open chrome browser

from selenium import webdriver
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://google.com")
driver.maximize_window()

print(driver.current_url)
print(driver.title)
