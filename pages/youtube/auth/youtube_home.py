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
    def search(self, keyword: str, channel_name: str):
        """Search keyword"""
        self.clear(*self.txt_search)
        self.send_keys(*self.txt_search, keyword)

        self.click(*self.btn_search)
        self.wait_for_page_to_be_loaded()

        link_channel_nrobo_in_search_result = (By.XPATH,
                                               f"//ytd-channel-renderer//yt-formatted-string[text()='{channel_name}']")
        self.click(*self.link_channel_nrobo_in_search_result)
        self.wait_for_page_to_be_loaded()

        self.click(*self.tab_playlists)
        self.wait_for_page_to_be_loaded()

        if 'tour' in link_channel_nrobo_in_search_result:
            lnk_tour_travels_playlist = (By.CSS_SELECTOR, "a[title='8. Tours and Travels']")
            self.click(*lnk_tour_travels_playlist)
            self.wait_for_page_to_be_loaded()

        return PagePlaylists(self.driver, self.logger)
