import time
from .pages.main_page import MainPage
from .pages.document_page import DocumentPage
from .pages.webdriver_page import WebdriverPage
from selenium.webdriver.common.keys import Keys

link = "https://www.selenium.dev/"

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу Documentation
def test_open_documentation(browser):
    page = MainPage(browser, link)
    page.open_page()
    time.sleep(2)
    page.should_be_link_to_document_page()
    page.go_to_documentation()
    time.sleep(2)
    # Проверяем что это точно страница Documentation
    page = DocumentPage(browser, link)
    page.should_be_document_page()

# Тест проверяет, что пользователь может перейти слева в меню в страницу WebDriver
def test_open_webdriver_page(browser):
    link = 'https://www.selenium.dev/documentation/'
    page = DocumentPage(browser, link)
    # создает экземпляр страницы Documentation
    page.open_page()
    time.sleep(2)
    page.go_to_webdriver()
    page = WebdriverPage(browser, link)
    time.sleep(2)
    page.should_be_webdriver_link()

def test_should_use_search(browser):
    page = MainPage(browser, link)
    page.open_page()
    time.sleep(2)
    page.should_be_search_btn()
    time.sleep(5)
    page.use_search(search=str('Blog'))
    time.sleep(5)


