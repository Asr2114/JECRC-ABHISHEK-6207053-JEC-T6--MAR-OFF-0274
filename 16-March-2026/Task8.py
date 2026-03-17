from selenium import webdriver
import time

driver = webdriver.Chrome()

websites = [
    "https://www.thesouledstore.com",
    "https://www.nike.com",
    "https://www.bbc.com/news",
    "https://www.python.org"
]

for site in websites:
    driver.get(site)
    time.sleep(3)
    print("Title:", driver.title)

driver.quit()