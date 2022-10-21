from selenium.webdriver.common.by import By

class MainPageLocators():

    DOCUMENT_LINK = (By.XPATH, "//a[@href='/documentation']")
    SEARCH_BTN = (By.XPATH, '//*[@id="docsearch"]/button/span[1]/span')

class DocumPageLocators():

    MENU_LINK = (By.XPATH, "//span[@class='td-sidebar-nav-active-item']")
    WEBDRIVER_LINK = (By.XPATH, '//*[@id="m-documentationwebdriver"]')

class SearchLocators():
    OPEN_SEARCH = (By.XPATH, '//*[@id="docsearch-input"]')
