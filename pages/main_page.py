from .locators import MainPageLocators
from .base_page import BasePage
from .locators import SearchLocators


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
        search_input.send_keys(search)
        self.browser.implicitly_wait(5)
        self.browser.find_element(*SearchLocators.ENTER_SEARCH).click()
        self.browser.implicitly_wait(0.5)


    def should_be_link_to_about_menu(self):
        assert self.element_is_present(*MainPageLocators.ABOUT_LINK)

    def go_to_about_menu(self):
        self.browser.find_element(*MainPageLocators.ABOUT_LINK).click()

    def should_be_link_to_history(self):
        assert self.element_is_present(*MainPageLocators.HISTORY_LINK)

    def go_to_history(self):
        self.browser.find_element(*MainPageLocators.HISTORY_LINK).click()