from .locators import MainPageLocators
from .base_page import BasePage
from .locators import SearchLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def should_be_link_to_document_page(self):
        assert self.element_is_present(*MainPageLocators.DOCUMENT_LINK)

    def go_to_documentation(self):
        self.browser.find_element(*MainPageLocators.DOCUMENT_LINK).click()

    def should_be_search_btn(self):
        assert self.element_is_present(*MainPageLocators.SEARCH_BTN)

    def use_search(self, search):
        self.browser.find_element(*MainPageLocators.SEARCH_BTN).click()
        search_input = self.browser.find_element(*SearchLocators.OPEN_SEARCH)
        search_input.send_keys(search + Keys.ENTER)

