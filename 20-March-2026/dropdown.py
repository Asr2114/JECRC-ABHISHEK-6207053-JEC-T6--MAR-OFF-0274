from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("file:///Users/asr2114/Desktop/Robot Python/20-March-2026/playlist.html")

driver.maximize_window()

songs_list = driver.find_element(By.ID, 'songs')
select = Select(songs_list)

if select.is_multiple:
    select.select_by_visible_text('Shape of You')
    select.select_by_visible_text('Animals')

print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()

time.sleep(5)
driver.quit()