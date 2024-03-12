from selenium.webdriver.common.by import By

from pages import Page


class PageGmailLogin(Page):
    """Gmail Login page"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    # Page element definitions

    # Page methods
    def open_gmail_login_url(self):
        """Open Gmail Login url"""

        self.get('https://accounts.google.com/servicelogin?hl=en-gb')

        return PageGmailLoginEmailOrPhone(driver=self.driver, logger=self.logger)


class PageGmailLoginEmailOrPhone(Page):
    """Gmail Login Email or Phone page"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    # Page elements
    txt_email_or_phone = (By.CSS_SELECTOR, "[type='email']")

    btn_next = (By.XPATH, "//span[text()='Next']/..")

    # Page methods
    def email_or_phone(self, email_or_phone):
        """Type given email or phone"""
        self.wait_for_a_while(self.generate_random_numbers(2, 5))
        self.send_keys(*self.txt_email_or_phone, email_or_phone)

    def next(self):
        """Click on Next button"""
        self.wait_for_a_while(self.generate_random_numbers(2, 5))
        self.click(*self.btn_next)

        return PageGmailLoginPassword(driver=self.driver, logger=self.logger)


class PageGmailLoginPassword(Page):
    """Gmail Login Email or Phone page"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    # Page elements
    txt_password = (By.CSS_SELECTOR, "[type='password']")

    btn_next = (By.XPATH, "//span[text()='Next']/..")

    # Page methods
    def password(self, password):
        """Type given password"""
        self.wait_for_a_while(self.generate_random_numbers(2, 5))
        self.send_keys(*self.txt_password, password)

    def next(self):
        """Click on Next button"""
        self.wait_for_a_while(self.generate_random_numbers(2, 5))
        self.click(*self.btn_next)

        self.wait_for_a_while(self.generate_random_numbers(2, 5))
        self.get('https://gmail.com')

        return PageGmailMailBox(driver=self.driver, logger=self.logger)


class PageGmailMailBox(Page):
    """Gmail Mailbox page"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)
