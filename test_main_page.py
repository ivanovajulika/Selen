import time

from .pages.main_page import MainPage
from .pages.document_page import DocumentPage
from .pages.webdriver_page import WebdriverPage
from pages.history_page import HistoryPage


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

# Тест проверяет, что пользователь может перейти с главной страницы сайта по кнопке 'READ MORE'
# на страницу WebDriver
def test_open_readmore_webdriver(browser):
    page = MainPage(browser, link)
    page.open_page()
    time.sleep(2)
    page.should_be_readmore_btn()
    page.go_to_readmore()
    time.sleep(2)
    # Проверяем что это точно страница WebDriver
    page = WebdriverPage(browser, link)
    page.should_be_webdriver_link()

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу Selenium History
def test_open_history(browser):
    page = MainPage(browser, link)
    page.open_page()
    time.sleep(2)
    page.should_be_link_to_about_menu()
    page.go_to_about_menu()
    time.sleep(2)
    #Переходим на страницу History
    page.should_be_link_to_history()
    page.go_to_history()
    # Проверяем что это точно страница History
    page = HistoryPage(browser, link)
    page.should_be_history_link()

    
# Тест проверяет, что пользователь может перейти слева в меню на страницу WebDriver
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

# Тест проверяет, что пользователь может ввести слово в поиск и перейти по нему
def test_should_use_search(browser):
    page = MainPage(browser, link)
    page.open_page()
    time.sleep(2)
    page.should_be_search_btn()
    time.sleep(2)
    page.use_search(search='grid')
    time.sleep(10)


