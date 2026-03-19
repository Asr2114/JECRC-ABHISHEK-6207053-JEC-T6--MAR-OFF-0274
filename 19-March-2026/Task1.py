from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demo.mobiscroll.com/select/multiple-select")


##-------------------------------------------

# driver.get("https://abc.com")
#
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 30)


# banners = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='hero-items']//picture/img")))
# links = []
#
# for banner in banners:
#     src = banner.get_attribute("src")
#     if src:
#         links.append(src)
#
# print("Banner Links: ")
# for link in links:
#
#     print(link)

driver.quit()