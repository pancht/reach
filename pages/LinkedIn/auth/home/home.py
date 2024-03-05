from selenium.webdriver.common.by import By

from pages import Page
from pages.LinkedIn.auth.home.single_post import PageSinglePost


class PageHome(Page):
    """LinkedIn Home Page Class After user log's in"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    # Page Elements
    btn_start_a_post_try_writing_with_ai = (By.CSS_SELECTOR, '.share-box-feed-entry__trigger')

    # Page methods
    def open_post_link(self, post_url):
        """Opens direct link to post"""

        self.get(post_url)

        return PageSinglePost(self.driver, self.logger)