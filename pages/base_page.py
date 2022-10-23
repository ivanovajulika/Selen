from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By



class Logo_locators():
    LOGO = (By.ID, 'selenium_logo')

class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

# метод позволяет вернуться  c любой cтраницы на главную, кликнув по логотипу
    def go_to_main_paige(self):
        self.browser.find_element(*Logo_locators.LOGO).click()

