from selenium.webdriver.common.by import By

class MainPageLocators():

    DOCUMENT_LINK = (By.XPATH, "//a[@href='/documentation']")

class DocumPageLocators():

    MENU_LINK = (By.XPATH, "//span[@class='td-sidebar-nav-active-item']")
