from selenium.webdriver.common.by import By

from pages import Page


class PageAllRecentActivity(Page):
    """All recent activity page"""

    def __init__(self, driver, logger):
        super().__init__(driver=driver, logger=logger)

    btn_react_like = (By.CSS_SELECTOR, "button[aria-label='React Like'][aria-pressed='false']")

    def like_all_recent_posts(self):
        """Like all recent posts under recent actvity page"""

        all_likes = self.find_elements(*self.btn_react_like)

        for btn_like in all_likes:
            from nrobo.util.common import Common
            self.wait_for_a_while(Common.generate_random_numbers(2, 5))
            btn_like.click()
