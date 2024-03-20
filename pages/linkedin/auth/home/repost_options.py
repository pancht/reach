from selenium.webdriver.common.by import By

from pages import Page
from pages.linkedin.auth.home.post_modal import PagePostModal


class PageRePostOptions(Page):
    def __init__(self, driver, logger):
        super().__init__(driver=driver, logger=logger)

    btn_repost_with_your_thoughts = (By.XPATH,
                                     "//div[contains(@class, 'artdeco-dropdown__item') "
                                     "and @tabindex='0' and @role='button']")

    def repost_with_your_thoughts(self) -> PagePostModal:
        self.click(*self.btn_repost_with_your_thoughts)

        return PagePostModal(self.driver, self.logger)
