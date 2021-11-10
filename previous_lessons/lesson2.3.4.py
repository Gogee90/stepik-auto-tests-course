from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    btn.click()
    alert = browser.switch_to_alert()
    alert.accept()
    value = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(int(value.text)))
    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()
finally:
    time.sleep(15)
    browser.quit()
