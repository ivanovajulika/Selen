from .locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def should_be_link_to_document_page(self):
        assert self.element_is_present(*MainPageLocators.DOCUMENT_LINK)

    def go_to_documentation(self):
        self.browser.find_element(*MainPageLocators.DOCUMENT_LINK).click()
