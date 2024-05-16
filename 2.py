from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Получаем в переменную browser указатель на браузер
browser = webdriver.Chrome()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://www.demoblaze.com/')

# Ждем, пока кнопка "Log in" станет кликабельной
login_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, 'login2'))
)
login_button.click()

# Ждем, пока появится поле для ввода имени пользователя
username = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.ID, 'loginusername'))
)
username.send_keys('makoveev')

password = browser.find_element(by=By.ID, value='loginpassword')
password.send_keys('12345678')

# Кликаем на кнопку "Log in"
login_btn = browser.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
login_btn.click()

# Добавляем задержку на 20 секунд перед закрытием браузера
time.sleep(3)

# Находим все элементы с классом "nav-link"
nav_links = browser.find_elements(By.CLASS_NAME, "nav-link")

# Переходим на вторую ссылку с классом "nav-link"
nav_links[1].click()

time.sleep(3)

email = browser.find_element(by=By.ID, value='recipient-email')
email.send_keys('y-makoveev@mail.ru')

name = browser.find_element(by=By.ID, value='recipient-name')
name.send_keys('Yarik')

massage = browser.find_element(by=By.ID, value='message-text')
massage.send_keys('Hello')

time.sleep(1)

button = browser.find_element(By.XPATH, "//button[@onclick='send()']")
button.click()

time.sleep(10)
# Закрываем браузер
browser.close()
