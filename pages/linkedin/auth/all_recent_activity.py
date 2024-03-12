from nrobo.util.common import Common
from selenium.webdriver.common.by import By

from pages import Page


class PageAllRecentActivity(Page):
    """All recent activity page"""

    def __init__(self, driver, logger):
        super().__init__(driver=driver, logger=logger)

    hdr_all_activity = (By.CSS_SELECTOR, '.text-heading-large')
    btn_react_like = (By.CSS_SELECTOR, "button[aria-label='React Like'][aria-pressed='false']")

    def like_all_recent_posts(self, count_groups):
        """Like all recent posts under recent actvity page"""

        for count in range(int(count_groups)+10):
            self.wait_for_page_to_be_loaded()
            self.scroll_down()
            self.wait_for_a_while(Common.generate_random_numbers(1, 3))

        self.wait_for_a_while(Common.generate_random_numbers(1, 3))
        self.scroll_to_top()
        self.wait_for_a_while(Common.generate_random_numbers(2, 4))
        all_likes = self.find_elements(*self.btn_react_like)
        self.logger.info(f"Total un-reacted links = {len(all_likes)}")

        for btn_like in all_likes:
            self.wait_for_a_while(Common.generate_random_numbers(2, 4))
            self.find_element(*self.btn_react_like).click()
