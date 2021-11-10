from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # link = "http://suninjuly.github.io/math.html"
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()

    browser.get(link)

    formula = browser.find_element_by_id("treasure")
    value = formula.get_attribute("valuex")

    print(value)

    # print(formulas.get_attribute("valuex"))

    # x = [formula.get_attribute("valuex") for formula in formulas]

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(int(value))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    robots_rule_check_box = browser.find_element(By.ID, "robotsRule")
    robots_rule_check_box.click()

    submit_btn = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_btn.click()
finally:
    time.sleep(10)
    browser.quit()
