from .base_page import BasePage

class HistoryPage(BasePage):

    def should_be_history_link(self):
        assert 'history' in self.browser.current_url, 'wrong url'