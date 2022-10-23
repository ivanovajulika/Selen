from selenium.webdriver.common.by import By

class MainPageLocators():

    DOCUMENT_LINK = (By.XPATH, "//a[@href='/documentation']")
    SEARCH_BTN = (By.XPATH, '//*[@id="docsearch"]/button/span[1]/span')
    WEBDRIVER_BTN = (By.XPATH, '/html/body/div/main/section[2]/div/div/div[1]/div/div[2]/div/a')
    ABOUT_LINK = (By.XPATH, '//*[@id="main_navbar"]/ul/li[2]')
    HISTORY_LINK = (By.XPATH, '//*[@id="main_navbar"]/ul/li[2]/div/a[5]')

class DocumPageLocators():

    MENU_LINK = (By.XPATH, "//span[@class='td-sidebar-nav-active-item']")
    WEBDRIVER_LINK = (By.XPATH, '//*[@id="m-documentationwebdriver"]')

class SearchLocators():
    OPEN_SEARCH = (By.XPATH, '//*[@id="docsearch-input"]')
    ENTER_SEARCH = (By.CSS_SELECTOR, '#docsearch-item-0 > a > div > div.DocSearch-Hit-action > svg')
