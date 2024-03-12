from selenium.webdriver.common.by import By

from pages import Page
from pages.youtube.auth.watch_playlist_view import PageWatchPlaylist


class PagePlaylists(Page):
    """Playlists page class"""

    def __init__(self, driver, logger):
        """constructor"""

        super().__init__(driver=driver, logger=logger)

    # Page elements
    lnk_view_nrobo_full_playlist = (By.XPATH,
                                    "//div[contains(@class,'ytd-grid-playlist-rendere')]"
                                    "/h3/a[@title='nRoBo Test Automation Framework']")

    lnk_play_all_nrobo_videos = (By.CSS_SELECTOR,
                                 ".thumbnail-and-metadata-wrapper a[aria-label='Play all']")

    # Page methods
    def click_link_view_nrobo_full_playlist(self):
        """Click on View nRoBo full playlist"""
        self.click(*self.lnk_view_nrobo_full_playlist)
        self.wait_for_a_while(4)
        self.wait_for_page_to_be_loaded()

    def click_play_all(self):
        """Click play all link"""

        self.click(*self.lnk_play_all_nrobo_videos)
        self.wait_for_page_to_be_loaded()

        return PageWatchPlaylist(self.driver, self.logger)

