from selenium import webdriver
import time
import math

# link = "http://suninjuly.github.io/find_link_text"
# link = "http://suninjuly.github.io/find_xpath_form"
# # link = "http://suninjuly.github.io/simple_form_find_task.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     # href = browser.find_element_by_link_text(
#     #     str(math.ceil(math.pow(math.pi, math.e) * 10000))
#     # )
#     # print(href)
#     # href.click()
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath("//button[text()='Submit']")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name("input")
#     for element in elements:
#         element.send_keys("Мой ответ")

#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# не забываем оставить пустую строку в конце файла
from selenium import webdriver
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector(".first_block .first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element_by_css_selector(".first_block .second")
    last_name.send_keys("Petrov")

    email = browser.find_element_by_css_selector(".first_block .third")
    email.send_keys("ivan.petrov@test.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
