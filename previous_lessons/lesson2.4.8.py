from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    input_value = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(int(input_value.text)))

    submit_btn = browser.find_element_by_id("solve")
    submit_btn.click()

finally:
    time.sleep(20)
    browser.quit()
