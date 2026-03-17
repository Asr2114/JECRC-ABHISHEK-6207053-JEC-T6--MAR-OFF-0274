from selenium import webdriver
import time

browsers = {
    "Chrome": webdriver.Chrome(),
    "Edge": webdriver.Edge(),
    "Firefox": webdriver.Firefox()
}

for name, browser in browsers.items():
    browser.get("https://www.wikipedia.org/")
    browser.maximize_window()

    time.sleep(2)

    print("Browser:", name)
    print("Title:", browser.title)
    print("URL:", browser.current_url)
    print("-" * 30)

    browser.quit()