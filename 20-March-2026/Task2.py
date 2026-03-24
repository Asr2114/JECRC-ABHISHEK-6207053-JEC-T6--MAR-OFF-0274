from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("file:///Users/asr2114/Desktop/Robot Python/20-March-2026/playlist.html")

driver.maximize_window()

dropdown = Select(driver.find_element(By.ID, 'songs'))

select_flag = False

for option in dropdown.options:
    text = option.text.strip().lower()

    if "alan walker" in text:
        select_flag = True
        continue

    if select_flag:
        if not option.is_enabled():
            break
        option.click()



selected_songs = [i.text for i in dropdown.all_selected_options]

print("Alan Walker Songs:")

for song in selected_songs:
    print(song)

driver.find_element(By.XPATH, "//button[text()='Add to Playlist']").click()

time.sleep(5)
driver.quit()



