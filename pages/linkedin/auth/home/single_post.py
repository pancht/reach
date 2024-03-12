from selenium.webdriver.common.by import By

from pages import Page
from pages.linkedin.auth.home.repost_options import PageRePostOptions


class PageSinglePost(Page):
    """Page class for Single Post Page"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    # Page Elements
    btn_repost = (By.CLASS_NAME, 'social-reshare-button')

    # Page methods
    def repost(self) -> PageRePostOptions:
        """Click on Repost button"""
        self.click(*self.btn_repost)
        return PageRePostOptions(self.driver, self.logger)


