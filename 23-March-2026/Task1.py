from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

driver.get("https://gameofthronesstudiotour.com/the-experience/")

driver.maximize_window()
action = ActionChains(driver)

ele = driver.find_element(By.CLASS_NAME, 'events_box_content')

action.scroll_to_element(ele)

time.sleep(4)


for _ in range(5):
    action.send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)


