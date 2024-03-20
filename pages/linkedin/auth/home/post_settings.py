from selenium.webdriver.common.by import By

from pages import Page
from pages.linkedin.auth.home.select_a_group import PageSelectAGroup


class PagePostSettings(Page):

    def __init__(self, driver, logger):
        super().__init__(driver=driver, logger=logger)

    # elements
    opt_groups = (By.CSS_SELECTOR, ".sharing-shared-generic-list__caret-wrapper ")

    btn_back = (By.XPATH, "//span[text()='Back']/..")
    btn_done = (By.CSS_SELECTOR, '.share-box-footer__primary-btn')

    # methods
    def select_groups(self) -> PageSelectAGroup:
        self.click(*self.opt_groups)

        return PageSelectAGroup(self.driver, self.logger)

    def post(self):
        self.click(*self.btn_done) if self.is_enabled(*self.btn_done) else self.click(*self.btn_back)

        from pages.linkedin.auth.home.post_modal import PagePostModal
        return PagePostModal(self.driver, self.logger)
