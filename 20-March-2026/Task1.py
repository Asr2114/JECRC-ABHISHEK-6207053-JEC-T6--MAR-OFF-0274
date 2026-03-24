from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("file:///Users/asr2114/Desktop/Robot Python/20-March-2026/playlist.html")

driver.maximize_window()

dropdown = Select(driver.find_element(By.ID, 'songs'))

for option in dropdown.options:
    text = option.text.lower()

    if "girl" in text or "love" in text:
        dropdown.select_by_visible_text(option.text)
print([i.text for i in dropdown.all_selected_options])

driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()

time.sleep(6)
driver.quit()