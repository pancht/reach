from selenium.webdriver.common.by import By

from pages import Page
from pages.linkedin.auth.home.post_settings import PagePostSettings


class PagePostModal(Page):

    def __init__(self, driver, logger):
        super().__init__(driver=driver, logger=logger)

    # Page Elements of Share Box modal
    btn_post_options = (By.CSS_SELECTOR, '.artdeco-entity-lockup__title')
    box_content = (By.CSS_SELECTOR, '.editor-content')
    txt_editor = (By.CSS_SELECTOR, "[data-placeholder='Start writing or use @ to mention people, companies or schools']")

    btn_post = (By.CSS_SELECTOR, '.share-actions__primary-action')
    btn_close_modal = (By.CSS_SELECTOR, "[href='#close-medium']")
    btn_discard = (By.XPATH, "//span[text()='Discard']/..")

    # Page methods of Share Box modal
    def write_thought(self, thought):
        self.send_keys(*self.txt_editor, thought)

    def post_to_groups(self) -> PagePostSettings:
        self.click(*self.btn_post_options)

        return PagePostSettings(self.driver, self.logger)

    def post(self) -> Page:
        self.click(*self.btn_post)
        self.wait_for_a_while(2)

        if self.is_displayed(*self.btn_post):
            self.click(*self.btn_close_modal)

        if self.is_displayed(*self.btn_discard):
            self.click(*self.btn_discard)

        from pages.linkedin.auth.home.single_post import PageSinglePost
        return PageSinglePost(self.driver, self.logger)

    def close(self):
        self.click(*self.btn_close_modal)

    def discard(self):
        if self.is_displayed(*self.btn_discard):
            self.click(*self.btn_discard)
