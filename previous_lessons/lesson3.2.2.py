from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

try:
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    print(num1.text, num2.text)
    select = Select(browser.find_element_by_tag_name("select"))
    summary = int(num1.text) + int(num2.text)
    select.select_by_value(str(summary))
    btn = browser.find_element_by_class_name("btn-default")
    btn.click()
finally:
    time.sleep(10)
    browser.quit()
