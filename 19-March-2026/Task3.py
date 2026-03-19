from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

search = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

# simulate typing
search.send_keys("lap")
time.sleep(1)
search.send_keys("top")

# wait for suggestion container (not items)
wait.until(EC.presence_of_element_located((By.ID, "nav-flyout-searchAjax")))

# now fetch suggestions
suggestions = driver.find_elements(By.XPATH, "//div[@id='nav-flyout-searchAjax']//div[@role='row']")

# click 4th suggestion
suggestions[3].click()

sort = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Sort')]")))
sort.click()

newest = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Newest')]")))
newest.click()


free_delivery = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Free')]")))
free_delivery.click()

product = wait.until(
    EC.presence_of_element_located((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]"))
)

name = product.find_element(By.XPATH, ".//h2").get_attribute("innerText")
price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").get_attribute("innerText")

print("Product:", name)
print("Price:", price)

driver.quit()