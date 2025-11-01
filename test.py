from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# поменяй URL для проверки (registration1.html — должен пройти, registration2.html — должен упасть)
url = "http://suninjuly.github.io/registration1.html"
# url = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    browser.get(url)

    # === УНИКАЛЬНЫЕ СЕЛЕКТОРЫ (пример, проверь в инспекторе страницы и при необходимости поправь) ===
    # Эти селекторы корректны для классической версии задания:
    browser.find_element(By.CSS_SELECTOR, "div.first_block .first").send_keys("Alex")
    browser.find_element(By.CSS_SELECTOR, "div.first_block .second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "div.first_block .third").send_keys("test@example.com")
    # ========================================================================================

    # Нажать кнопку Submit (на обеих страницах кнопка есть, но нас интересуют поля)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Подождать, вывести результат (если появится код)
    time.sleep(3)
    # пытаемся получить текст с итоговой страницы
    print(browser.find_element(By.TAG_NAME, "h1").text)

finally:
    # даём время, чтобы скопировать код (если нужен) - можно уменьшить
    time.sleep(5)
    browser.quit()
