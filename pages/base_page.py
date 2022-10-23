from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class SearchLocators():
    OPEN_SEARCH = (By.XPATH, '//*[@id="docsearch-input"]')
    ENTER_SEARCH = (By.XPATH, '')


class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.maximize_window()
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True