from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
service = Service()
options = Options()

for i in range(3):
    print(f"Iteration {i+1}")

    driver = webdriver.Firefox(service = service, options = options)

    driver.get("https://www.amazon.in/")

    time.sleep(2)


    driver.maximize_window()
    print("Browser Maximised")
    time.sleep(2)

    driver.minimize_window()
    print("Browser Minimized")
    time.sleep(2)

    driver.maximize_window()
    print("Browser Maximized Again")
    time.sleep(2)

    driver.get("https://www.wikipedia.org")
    time.sleep(2)

    driver.back()
    print("Navigated Back")
    time.sleep(2)

    driver.forward()
    print("Navigated Forward")
    time.sleep(2)

    driver.refresh()
    print("Page Refreshed")
    time.sleep(2)


    driver.quit()
