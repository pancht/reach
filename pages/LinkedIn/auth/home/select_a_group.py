from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages import Page


class PageSelectAGroup(Page):

    def __init__(self, driver, logger):
        super().__init__(driver=driver, logger=logger)

    lstGroups = (By.CSS_SELECTOR, ".sharing-shared-generic-list__item")
    lst_group_names = (By.CSS_SELECTOR, ".sharing-shared-generic-list__description-single-line")

    btn_back = (By.XPATH, "//span[text()='Back']/..")
    btn_save = (By.CSS_SELECTOR, '.share-box-footer__primary-btn')

    def group_names(self) -> list[str]:
        groups = self.find_elements(*self.lst_group_names)
        names = []
        [names.append(group.text) for group in groups]

        return names

    def select_a_group_and_save(self, group_name: str) -> Page:
        # select a group
        group_element_by_name = self.find_element(By.XPATH, f"//fieldset//span[text()='{group_name}']")
        group_element_by_name.click()

        self.wait_for_a_while(1)
        self.click(*self.btn_save) if self.is_enabled(*self.btn_save) else self.click(*self.btn_back)

        from pages.LinkedIn.auth.home.post_settings import PagePostSettings
        return PagePostSettings(self.driver, self.logger)
