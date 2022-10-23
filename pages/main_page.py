from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver import Keys
class MainPageLocators():

    DOCUMENT_LINK = (By.XPATH, "//a[@href='/documentation']")
    SEARCH_BTN = (By.XPATH, '//*[@id="docsearch"]/button/span[1]/span')
    WEBDRIVER_BTN = (By.XPATH, '/html/body/div/main/section[2]/div/div/div[1]/div/div[2]/div/a')
    ABOUT_LINK = (By.XPATH, '//*[@id="main_navbar"]/ul/li[2]')
    HISTORY_LINK = (By.XPATH, '//*[@id="main_navbar"]/ul/li[2]/div/a[5]')

class SearchLocators():
    OPEN_SEARCH = (By.XPATH, '//*[@id="docsearch-input"]')
    ENTER_SEARCH = (By.XPATH, '')


class MainPage(BasePage):

    def should_be_link_to_document_page(self):
        assert self.element_is_present(*MainPageLocators.DOCUMENT_LINK)

    def go_to_documentation(self):
        self.browser.find_element(*MainPageLocators.DOCUMENT_LINK).click()

    def should_be_readmore_btn(self):
        assert self.element_is_present(*MainPageLocators.WEBDRIVER_BTN)

    def go_to_readmore(self):
        self.browser.find_element(*MainPageLocators.WEBDRIVER_BTN).click()

    def should_be_search_btn(self):
        assert self.element_is_present(*MainPageLocators.SEARCH_BTN)

    def use_search(self, search):
        self.browser.find_element(*MainPageLocators.SEARCH_BTN).click()
        search_input = self.browser.find_element(*SearchLocators.OPEN_SEARCH)
        search_input.send_keys(search + Keys.ENTER)

    def should_be_link_to_about_menu(self):
        assert self.element_is_present(*MainPageLocators.ABOUT_LINK)

    def go_to_about_menu(self):
        self.browser.find_element(*MainPageLocators.ABOUT_LINK).click()

    def should_be_link_to_history(self):
        assert self.element_is_present(*MainPageLocators.HISTORY_LINK)

    def go_to_history(self):
        self.browser.find_element(*MainPageLocators.HISTORY_LINK).click()