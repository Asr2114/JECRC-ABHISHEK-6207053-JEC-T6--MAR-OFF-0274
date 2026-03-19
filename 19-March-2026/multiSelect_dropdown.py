from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)


# driver.get("https://www.abc.com")
#
# driver.maximize_window()
#
#
#
# wait = WebDriverWait(driver, 10)
#
# loading_circles = wait.until(EC.invisibility_of_element_located((By.ID, 'preloader-animated_svg__circles')))
#
# title_abc = driver.find_element(By.XPATH, '//span[text()="ABC SHOWS, SPECIALS & MORE"]')
#
# assert 'SPECIALS' in title_abc.text, 'the text not present'
#
# print('working fine')


## ------=-----------------------

driver.get("https://demoqa.com/dynamic-properties")
driver.maximize_window()

wait = WebDriverWait(driver, 6)
enable_before = driver.find_element(By.ID, 'enableAfter')


print(enable_before.is_enabled())

enable_btn = wait.until(EC.element_to_be_clickable((By.ID, 'enableAfter')))

if enable_btn.is_enabled():
    enable_btn.click()
    print(enable_btn.text)


visible_ele = wait.until(EC.visibility_of_element_located((By.ID, 'visibleAfter')))
visible_ele.click()



# ele = driver.find_element(By.XPATH, '(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
# # search.send_keys("Selenium")

#
# # print(ele.get_attribute('src'))
#
# # wait_obj = WebDriverWait(driver, 10, poll_frequency=200)
#
# submit_button = wait_obj.until(EC.element_to_be_clickable((By.ID, 'button')))
# submit_button.click()



driver.quit()



## explicitly wait
## it is confined to the particular element
## we have to import two things , webdriverwait and expected conditions


