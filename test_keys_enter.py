from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_go_to_translator():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.google.ru/")

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()
    
    text_box.send_keys("Переводчик"+Keys.ENTER)

    driver.implicitly_wait(0.5)

    driver.quit()
