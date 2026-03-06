from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()

try:
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    print("Цена достигла $100!")

    book_button = driver.find_element(By.ID, "book")
    book_button.click()

    x_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = int(x_element.text)

    result = calc(x)

    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    result_alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    answer = result_alert.text
    print(f"Число для ответа: {answer}")

    result_alert.accept()

finally:
    driver.quit()