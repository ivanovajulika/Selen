from .base_page import BasePage
from selenium.webdriver.common.by import By
class DocumPageLocators():

    MENU_LINK = (By.XPATH, "//span[@class='td-sidebar-nav-active-item']")
    WEBDRIVER_LINK = (By.XPATH, '//*[@id="m-documentationwebdriver"]')

class DocumentPage(BasePage):

    def should_be_document_page(self):
        self.should_be_document_link()
        self.should_be_menu_document()

    def should_be_document_link(self):
        assert 'documentation' in self.browser.current_url, 'wrong url'

    def should_be_menu_document(self):
        assert self.element_is_present(*DocumPageLocators.MENU_LINK)

    def go_to_webdriver(self):
        self.browser.find_element(*DocumPageLocators.WEBDRIVER_LINK).click()

