from selenium.webdriver.common.by import By

class MainPageLocators():

    DOCUMENT_LINK = (By.XPATH, "//a[@href='/documentation']")
    SEARCH_BTN = (By.XPATH, '//*[@id="docsearch"]/button/span[1]/span')
    WEBDRIVER_BTN = (By.XPATH, 'a[href="/documentation/webdriver/"]')
    ABOUT_LINK = (By.XPATH, '//*[@id="main_navbar"]/ul/li[2]')
    HISTORY_LINK = (By.XPATH, '//*[@href="/history"]')

class DocumPageLocators():

    MENU_LINK = (By.XPATH, '//*[@id="m-documentation"]/span')
    WEBDRIVER_LINK = (By.XPATH, '//*[@id="m-documentationwebdriver"]')

class SearchLocators():
    OPEN_SEARCH = (By.XPATH, '//*[@id="docsearch-input"]')
    ENTER_SEARCH = (By.XPATH, '//*[@id="docsearch-item-0"]/a/div/div[3]')
