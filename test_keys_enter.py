from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# TestData
link = "https://www.saucedemo.com/"
standard_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
performance_glitch_user = "performance_glitch_user"
password = "secret_sauce"


def test_password_is_empty():
    password_empty = ""
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get(link)
    browser.implicitly_wait(10)

    username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username_input.send_keys(standard_user)
    password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password_empty)
    btn_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    btn_login.click()
    browser.implicitly_wait(10)
    assert "inventory" not in browser.current_url, "Wrong page"
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text == "Epic sadface: Password is required"
    ), "Wrong error message"
    browser.quit()
