from .locators import DocumPageLocators
from .base_page import BasePage

class DocumentPage(BasePage):

    def should_be_document_page(self):
        self.should_be_document_link()
        self.should_be_menu_document()

    def should_be_document_link(self):
        assert 'documentation' in self.browser.current_url, 'wrong url'

    def should_be_menu_document(self):
        assert self.element_is_present(*DocumPageLocators.MENU_LINK)

