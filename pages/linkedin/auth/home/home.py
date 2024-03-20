from selenium.webdriver.common.by import By

from pages import Page
from pages.linkedin.auth.all_recent_activity import PageAllRecentActivity
from pages.linkedin.auth.home.single_post import PageSinglePost


class PageHome(Page):
    """linkedin Home Page Class After user log's in"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    # Page Elements
    message_window_header = (By.CSS_SELECTOR, ".msg-overlay-bubble-header")
    btn_start_a_post_try_writing_with_ai = (By.CSS_SELECTOR, '.share-box-feed-entry__trigger')

    # Page methods
    def collapse_message_window_header(self):
        """Collapse messaging header window

           by clicking on messaging chevron down small icon"""
        self.click(*self.message_window_header)

    def open_post_link(self, post_url):
        """Opens direct link to post"""

        self.get(post_url)

        return PageSinglePost(self.driver, self.logger)

    def open_all_activity_link(self, all_activity_url):
        """Opens all activity link to post"""

        self.get(all_activity_url)

        return PageAllRecentActivity(self.driver, self.logger)
