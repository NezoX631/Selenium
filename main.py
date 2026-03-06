from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    """Вычисляет математическую функцию от x"""
    return str(math.log(abs(12 * math.sin(int(x)))))


# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # Открываем нужную страницу
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидаем появления цены $100 на странице (максимум 12 секунд)
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    print("Цена достигла $100!")

    # Находим кнопку "Book" и нажимаем её
    book_button = driver.find_element(By.ID, "book")
    book_button.click()

    # Ожидаем появления элемента с числом x для вычислений
    x_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = int(x_element.text)  # Получаем значение x и преобразуем в целое число

    # Вычисляем результат математической функции
    result = calc(x)

    # Находим поле для ввода ответа и вводим результат
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Находим кнопку отправки и нажимаем её
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ожидаем появления alert с результатом
    result_alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    answer = result_alert.text  # Получаем текст из alert
    print(f"Число для ответа: {answer}")

    # Принимаем alert (закрываем его)
    result_alert.accept()

finally:
    # Закрываем браузер после выполнения всех действий
    driver.quit()
