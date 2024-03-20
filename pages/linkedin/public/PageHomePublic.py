from nrobo.util.common import Common
from selenium.webdriver.common.by import By

from pages import Page
from pages.linkedin.auth.home.home import PageHome


class PageHomePublic(Page):
    """Page class for linkedin Home Page"""

    def __init__(self, driver, logger):
        """constructor"""
        super().__init__(driver=driver, logger=logger)

    # linkedin Home Page Elements
    txt_email_or_phone = (By.ID, 'session_key')
    txt_password = (By.ID, 'session_password')

    btn_sign_in = (By.CSS_SELECTOR, "[data-id='sign-in-form__submit-btn']")
    btn_verify = (By.XPATH, "//button[text()='Verify']")

    # Page Methods
    def login(self, email_or_phone, password) -> PageHome:
        """linkedin Page Method For Login"""

        self.wait_for_a_while(Common.generate_random_numbers(3, 10))
        self.send_keys(*self.txt_email_or_phone, email_or_phone)
        self.wait_for_a_while(Common.generate_random_numbers(2, 7))
        self.send_keys(*self.txt_password, password)

        self.wait_for_a_while(Common.generate_random_numbers(2, 4))
        self.click(*self.btn_sign_in)
        self.wait_for_a_while(Common.generate_random_numbers(2, 4))

        if self.is_displayed(*self.btn_verify):
            self.wait_for_a_while(Common.generate_random_numbers(2, 4))
            self.click(*self.btn_verify)

        if self.is_displayed(*self.txt_email_or_phone):
            self.wait_for_a_while(Common.generate_random_numbers(20, 60))
            self.wait_for_a_while(Common.generate_random_numbers(3, 10))
            self.send_keys(*self.txt_email_or_phone, email_or_phone)
            self.wait_for_a_while(Common.generate_random_numbers(2, 7))
            self.send_keys(*self.txt_password, password)

            self.wait_for_a_while(Common.generate_random_numbers(2, 4))
            self.click(*self.btn_sign_in)
            self.wait_for_a_while(Common.generate_random_numbers(2, 4))

        return PageHome(driver=self.driver, logger=self.logger)
