from .base_page import BasePage


class WebdriverPage(BasePage):
    def should_be_webdriver_link(self):
        assert "webdriver" in self.browser.current_url, "wrong url"
