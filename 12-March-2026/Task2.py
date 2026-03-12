from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

from selenium.webdriver.firefox.options import Options as FirefoxOptions


chrome_service = ChromeService()
firefox_service = FirefoxService()

chrome_options = ChromeOptions()
firefox_options = FirefoxOptions()

chrome = webdriver.Chrome(service = chrome_service, options = chrome_options)
firefox = webdriver.Firefox(service=firefox_service, options=firefox_options)

chrome.get("https://www.amazon.in/")
firefox.get("https://www.amazon.in/")

time.sleep(2)

chrome.maximize_window()
firefox.maximize_window()
print("Browsers Maximized")
time.sleep(2)

chrome.minimize_window()
firefox.minimize_window()
print("Browsers Minimized")
time.sleep(2)

chrome.maximize_window()
firefox.maximize_window()
print("Browsers Maximized")
time.sleep(2)

chrome.get("https://www.wikipedia.org")
firefox.get("https://www.wikipedia.org")
time.sleep(2)

chrome.back()
firefox.back()
print("Browsers Back")
time.sleep(2)

chrome.forward()
firefox.forward()
print("Browsers Forward")
time.sleep(2)

chrome.refresh()
firefox.refresh()
print("Browsers Refresh")
time.sleep(2)

chrome.quit()
firefox.quit()
print("Browsers Quit")