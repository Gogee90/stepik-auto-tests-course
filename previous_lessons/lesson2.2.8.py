import time
from selenium import webdriver
import os

from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    first_name = browser.find_element(By.NAME, "firstname")
    last_name = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    upload_file = browser.find_element(By.NAME, "file")
    submit_btn = browser.find_element(By.CLASS_NAME, "btn-primary")

    first_name.send_keys("Ivan")
    last_name.send_keys("Govnov")
    email.send_keys("ivan.govnov@test.com")
    upload_file.send_keys(os.path.join(os.getcwd(), "test.txt"))

    submit_btn.click()
finally:
    time.sleep(10)
    browser.quit()
