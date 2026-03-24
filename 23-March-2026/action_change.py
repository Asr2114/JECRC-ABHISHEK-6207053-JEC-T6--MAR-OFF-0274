from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
# action = ActionChains(driver)

# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
#
# driver.maximize_window()
# time.sleep(2)



# origin_ele = driver.find_element(By.ID, 'column-a')
# target_ele = driver.find_element(By.ID, 'column-b')
#
# action.drag_and_drop(origin_ele, target_ele).perform()


#------------------------0>
#Hover element

# driver.get('https://supertails.com/')
# driver.maximize_window()
#
# time.sleep(2)
#
# doggo = driver.find_element(By.XPATH, '(//span[contains(text(), "Dogs")])[1]')
#
#
# action.move_to_element(doggo).perform()
#
# time.sleep(3)

##----------------------->

## Scroll to the element
#
# driver.get('https://supertails.com/')
# driver.maximize_window()
#
# time.sleep(2)
#
# scrollElement = driver.find_element(By.XPATH, '//div[@data-ganame="Breed 5"]')
#
# action.scroll_to_element(scrollElement).perform()
#
#
#
# time.sleep(5)
#
# action.scroll_by_amount(0, -1500).perform()
# time.sleep(5)


#-----------p-=>>>>

# Clicks
#
# Left Click = click()
# Right click = context_click()


# driver.quit()




##---------=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Keyboard actions
#
# driver = webdriver.Chrome()
# driver.get("https://amazon.in/")
# driver.maximize_window()
# action = ActionChains(driver)
#
# # action.send_keys(Keys.PAGE_UP).perform()
# # time.sleep(3)
# #
# # action.send_keys(Keys.PAGE_UP).perform()
# # time.sleep(3)
#
# action.key_down(Keys.COMMAND).send_keys('a').perform()
# time.sleep(3)
#
# action.key_up(Keys.COMMAND).perform()
# time.sleep(3)
#
# action.key_down(Keys.COMMAND).send_keys('c').perform()
# time.sleep(2)
#
# action.key_up(Keys.COMMAND).perform()
# time.sleep(2)
#
# # pasted = action.key_down(Keys.COMMAND).send_keys('v').key_up()
#
# driver.quit()

##3--=---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=
#
#
# driver = webdriver.Chrome()
# driver.get("file:///Users/asr2114/Desktop/Robot Python/23-March-2026/index.html")
# driver.maximize_window()
# action = ActionChains(driver)

# present = driver.find_element(By.ID, 'presentAddress')
# permanent = driver.find_element(By.ID, 'permanentAddress')
# present.send_keys('JECRC, Jaipur')
#
# time.sleep(3)
# present.click()
#
#
#
# action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
#
# time.sleep(2)
#
# action.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND).perform()
#
# time.sleep(2)
#
# permanent.click()
#
# action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
#
# time.sleep(2)
#
# driver.quit()


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

driver = webdriver.Chrome()
driver.get("file:///Users/asr2114/Desktop/Robot Python/23-March-2026/index1.html")
driver.maximize_window()
action = ActionChains(driver)

driver.find_element(By.ID, 'password').send_keys('Abhishek')
time.sleep(2)

show_pwd = driver.find_element(By.ID, 'eyeBtn')
action.click_and_hold(show_pwd).perform()

time.sleep(3)
action.release()



