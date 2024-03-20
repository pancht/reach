from selenium.webdriver.common.by import By

from pages import Page
from pages.youtube.auth.playlists import PagePlaylists


class PageYouTube(Page):
    """YouTube Page Class"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    # Page elements
    txt_search = (By.XPATH, "//input[@id='search']")

    btn_search = (By.ID, "search-icon-legacy")

    tab_playlists = (By.XPATH, "//div[@id='tabsContent']//div[text()='Playlists']")

    # Page methods
    def search(self, keyword: str, channel_name: str, playlist_name: str = None):
        """Search keyword"""
        self.wait_for_page_to_be_loaded()
        self.wait_for_a_while(self.generate_random_numbers(3, 7))

        self.clear(*self.txt_search)
        self.send_keys(*self.txt_search, keyword)
        self.click(*self.btn_search)
        self.wait_for_page_to_be_loaded()
        from nrobo.util.common import Common
        self.wait_for_a_while(Common.generate_random_numbers(3, 6))

        link_channel_search_result = (By.XPATH, f"//ytd-channel-renderer//yt-formatted-string[text()='{channel_name}']")
        print(f"current handle={self.current_window_handle}")
        self.click(*link_channel_search_result)
        self.wait_for_page_to_be_loaded()

        self.click(*self.tab_playlists)
        self.wait_for_page_to_be_loaded()

        if playlist_name is not None and 'Singh' in channel_name:
            lnk_playlist = (By.CSS_SELECTOR, f"a[title='{playlist_name}']")
            self.click(*lnk_playlist)
            self.wait_for_page_to_be_loaded()

        return PagePlaylists(self.driver, self.logger)
