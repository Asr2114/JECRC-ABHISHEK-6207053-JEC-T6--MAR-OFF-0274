from selenium import webdriver
import time

browsers = [
    webdriver.Chrome(),
    webdriver.Edge(),
    webdriver.Firefox()
]

for browser in browsers:
    browser.get("https://www.google.com")
    browser.maximize_window()
    time.sleep(3)
    browser.quit()