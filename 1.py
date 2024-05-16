from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
# Закрываем браузер
browser.close()
