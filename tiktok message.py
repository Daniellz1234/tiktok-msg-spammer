from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

friend_username = 'victims username'

user_data_dir = r'C:\Users\        \AppData\Local\Google\Chrome\User Data'
profile_dir = 'Default'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_dir}")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get('https://www.tiktok.com/')
    time.sleep(20)

    driver.get(f'https://www.tiktok.com/@{friend_username}')
    time.sleep(20)

    message_button = driver.find_element(By.XPATH, '//button[contains(text(), "Message")]')
    message_button.click()
    time.sleep(20)

    message_field = driver.find_element(By.XPATH, '//div[@data-e2e="message-input-area"]//div[@role="textbox"]')
    message_field.click()

    message_text = 'spammed'

    while True:
        message_field.send_keys(message_text)
        message_field.send_keys(Keys.RETURN)
        time.sleep(0.000000000000000000000000000000000000000000000000000000000001)

finally:
    driver.quit()
                #made by me daniellz1234