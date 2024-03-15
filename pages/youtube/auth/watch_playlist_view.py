from selenium.webdriver.common.by import By

from pages import Page


class PageWatchPlaylist(Page):
    """Watch Playlist page class"""

    # Page elements
    btn_loop_playlist = (By.CSS_SELECTOR, "ytd-page-manager button[aria-label='Loop playlist']")
    btn_playlist_un_shuffled = (
    By.CSS_SELECTOR, "ytd-page-manager button[aria-label='Shuffle playlist'][aria-pressed='false']")
    btn_playlist_shuffled = (
        By.CSS_SELECTOR, "ytd-page-manager button[aria-label='Shuffle playlist'][aria-pressed='true']")

    btn_i_like_this = (By.XPATH,
                       "//div[@id='actions-inner']//button[@title='I like this'][1]")

    # player controls
    div_player = (By.CSS_SELECTOR, "div[id='player']")
    btn_volume_control = (By.CSS_SELECTOR, "span.ytp-volume-area button[data-title-no-tooltip='Mute']")

    btn_settings_control = (By.CSS_SELECTOR, "button.ytp-settings-button")
    opt_playback_speed = (By.XPATH, "//div[contains(text(),'Playback speed')]")
    opt_playback_speed_2x = (By.XPATH, "//div[@class='ytp-menuitem-label' and text()='2']")

    # Page methods
    def click_loop_playlist_button(self):
        """Click on Loop Playlist button"""

        if self.is_displayed(*self.btn_loop_playlist):
            self.click(*self.btn_loop_playlist)
            self.wait_for_a_while(3)

    def click_shuffle_playlist_button(self):
        """Click on Shuffle Playlist button"""

        random_number = self.generate_random_numbers(3, 20)
        if random_number % 2 == 0:
            # if Even number, then choose shuffle playlist
            if self.is_displayed(*self.btn_playlist_un_shuffled):
                # if shuffle playlist not selected, then shuffle playlist
                self.click(*self.btn_playlist_un_shuffled)
                self.wait_for_a_while(3)
        else:
            # if odd number, then choose not to shuffle playlist
            if self.is_displayed(*self.btn_playlist_shuffled):
                # if shuffle playlist not selected, then shuffle playlist
                self.click(*self.btn_playlist_shuffled)
                self.wait_for_a_while(3)

    def click_like_video(self):
        """Like video if it is not yet liked by the current user"""
        try:
            if self.is_displayed(*self.btn_i_like_this):
                self.click(*self.btn_i_like_this)
                self.wait_for_a_while(3)
        except Exception as e:
            pass

    def current_playlist_is_nrobo(self):
        """Check if current playlist is nRoBo Test Automation Framework"""
        header_nrobo_test_automation_framework = (By.XPATH,
                                                  "//div[@id='secondary']"
                                                  "//h3//a[text()='nRoBo Test Automation Framework']")
        if self.is_displayed(*header_nrobo_test_automation_framework):
            return True

        return False

    def click_volume_control_and_set_playback_speed_2x(self):
        """Click volume control"""
        player = self.find_element(*self.div_player)
        btn_share = self.find_element(By.CSS_SELECTOR, "div[id='actions'] button[aria-label='Share']")

        if self.is_displayed(*self.btn_volume_control):
            try:
                self.action_chain() \
                    .pause(2).click(self.find_element(*self.btn_settings_control)) \
                    .perform()

                self.action_chain() \
                    .pause(2).click(self.find_element(*self.opt_playback_speed)) \
                    .perform()

                self.action_chain() \
                    .pause(2).click(self.find_element(*self.opt_playback_speed_2x)) \
                    .perform()

                self.action_chain() \
                    .move_to_element(player) \
                    .pause(2).click(self.find_element(*self.btn_settings_control)) \
                    .perform()

            except Exception as e:
                pass

        else:
            try:
                self.action_chain() \
                    .move_to_element(player) \
                    .pause(2).click(self.find_element(*self.btn_settings_control)) \
                    .perform()

                self.action_chain() \
                    .pause(2).click(self.find_element(*self.opt_playback_speed)) \
                    .perform()

                self.action_chain() \
                    .pause(2).click(self.find_element(*self.opt_playback_speed_2x)) \
                    .perform()

                self.action_chain() \
                    .move_to_element(player) \
                    .pause(2).click(self.find_element(*self.btn_settings_control)) \
                    .perform()
            except Exception as e:
                pass

        self.wait_for_page_to_be_loaded()
        self.wait_for_a_while(3)

    def click_settings_playback_speed_2x(self):
        """Click setting: Playback speed = 2x"""

        player = self.find_element(*self.div_player)
        self.action_chain() \
            .move_to_element(player) \
            .pause(2) \
            .perform()

        self.action_chain() \
            .click(self.find_element(*self.btn_settings_control)) \
            .pause(4).click(self.find_element(*self.opt_playback_speed)) \
            .pause(4).click(self.find_element(*self.opt_playback_speed_2x)) \
            .perform()
        self.wait_for_page_to_be_loaded()
        self.wait_for_a_while(3)
