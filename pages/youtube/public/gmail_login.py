from selenium.webdriver.common.by import By

from pages import Page
from pages.youtube.auth.youtube_home import PageYouTube


class PageGmailLogin(Page):
    """Gmail Login page"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    # Page element definitions

    # Page methods
    def open_gmail_login_url(self):
        """Open Gmail Login url"""

        self.get('https://accounts.google.com')
        self.wait_for_a_while(self.generate_random_numbers(3, 6))

        return PageGmailLoginEmailOrPhone(driver=self.driver, logger=self.logger)

    def gmail_login_through_stackoverflow(self, gmail_email, gmail_password):
        """Open Stackoverflow login"""

        self.get('https://stackoverflow.com/')
        self.wait_for_a_while(self.generate_random_numbers(2, 5))

        self.click(By.XPATH, "//a[text()='Log in']")
        self.wait_for_a_while(self.generate_random_numbers(2, 5))

        self.click(By.XPATH, "//button[@data-provider='google']")
        self.wait_for_a_while(self.generate_random_numbers(2, 5))
        self.wait_for_page_to_be_loaded()

        gmail_email_page = PageGmailLoginEmailOrPhone(self.driver, self.logger)
        gmail_email_page.email_or_phone(gmail_email)
        gmail_email_page.next()
        gmail_email_page.wait_for_page_to_be_loaded()

        gmail_password_page = PageGmailLoginPassword(self.driver, self.logger)
        gmail_password_page.password(gmail_password)
        gmail_password_page.next()
        gmail_password_page.wait_for_page_to_be_loaded()

        self.wait_for_a_while(self.generate_random_numbers(2, 5))
        self.click(By.XPATH, "//span[text()='Continue']/..")
        self.wait_for_a_while(self.generate_random_numbers(2, 5))

        self.get('https://gmail.com')
        self.wait_for_page_to_be_loaded()

        return PageGmailMailBox(self.driver, self.logger)


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
        self.wait_for_a_while(self.generate_random_numbers(2, 7))
        self.send_keys(*self.txt_email_or_phone, email_or_phone)

    def next(self):
        """Click on Next button"""
        self.wait_for_a_while(self.generate_random_numbers(3, 9))
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
        self.wait_for_a_while(self.generate_random_numbers(4, 6))
        self.send_keys(*self.txt_password, password)

    def next(self):
        """Click on Next button"""
        self.wait_for_a_while(self.generate_random_numbers(3, 8))
        self.click(*self.btn_next)

        self.wait_for_a_while(self.generate_random_numbers(2, 5))
        self.get('https://gmail.com')
        self.wait_for_a_while(self.generate_random_numbers(2, 5))

        return PageGmailMailBox(driver=self.driver, logger=self.logger)


class PageGmailMailBox(Page):
    """Gmail Mailbox page"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    lnk_google_apps = (By.XPATH, "//a[@aria-label='Google apps']")

    def open_youtube_url(self):
        """Open YouTube Url"""

        self.get('https://www.youtube.com/')
        self.wait_for_a_while(self.generate_random_numbers(2, 5))

        return PageYouTube(driver=self.driver, logger=self.logger)
