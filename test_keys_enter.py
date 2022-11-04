from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_go_translation():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get("https://www.google.ru/")

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(By.XPATH, value="//div/div[2]/input")
    text_box.send_keys("Переводчик" + Keys.ENTER)

    driver.implicitly_wait(3)

    driver.quit()
