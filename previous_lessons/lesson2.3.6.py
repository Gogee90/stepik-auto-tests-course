from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    trollface_btn = browser.find_element(By.CLASS_NAME, "trollface")
    trollface_btn.click()
    new_windows = browser.window_handles
    print(new_windows)
    browser.switch_to_window(new_windows[1])
    value = browser.find_element(By.ID, "input_value")
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(int(value.text)))
    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()
finally:
    time.sleep(15)
    browser.quit()
