import os

import pytest
from nrobo.util.common import Common

from pages import Page
from pages.linkedin.auth.home.post_modal import PagePostModal
from pages.linkedin.public.PageHomePublic import PageHomePublic
from pages.youtube.auth.playlists import PagePlaylists
from pages.youtube.auth.watch_playlist_view import PageWatchPlaylist
from pages.youtube.auth.youtube_home import PageYouTube
from pages.youtube.public.gmail_login import PageGmailLogin

counter_file = "Counter.yaml"
count_groups = "count_groups"

cred_yaml_file = 'cred.yaml'
test_data_yaml_file = 'test_data.yaml'

cred_data = Common.read_yaml(cred_yaml_file)
youtube_test_data = cred_data['youtube']
youtube_users = [(cred['username'], cred['password']) for cred in youtube_test_data]

channel_list = cred_data['youtube_channel_list']
keyword_list = cred_data['youtube_keyword_list']
playlist_list = cred_data['playlist_list']
channel_name_keyword_list = [(channel_list[idx], keyword_list[idx]) for idx, keyword in enumerate(keyword_list)]


class TestPostAndShareNRoBoUpdates:
    # @pytest.mark.run(order=1)
    @pytest.mark.linkedin
    def test_post_and_share_nrobo_updates_linkedin(self, driver, logger):
        """Post and share nRoBo updates on linkedin"""

        cred = Common.read_yaml(cred_yaml_file)
        data = Common.read_yaml(test_data_yaml_file)

        page_home_public = PageHomePublic(driver, logger)
        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 5))
        page_home_public.maximize_window()
        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 3))
        page_home_public.get(data['linkedin']['linkedin_url'])

        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 6))
        page_home = page_home_public.login(cred['linkedin']['username'], cred['linkedin']['password'])
        page_home.collapse_message_window_header()

        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 5))
        page_single_post = page_home.open_post_link(data['linkedin']['post_url'])

        repost_options = page_single_post.repost()

        post_modal = repost_options.repost_with_your_thoughts()

        post_settings_modal = post_modal.post_to_groups()

        select_a_group_modal = post_settings_modal.select_groups()
        select_a_group_modal.wait_for_a_while(Common.generate_random_numbers(1, 5))

        group_names = select_a_group_modal.group_names()
        # Common.write_yaml("groups.yaml", group_names)
        # exit()

        # Common.write_yaml(counter_file, {count_groups: len(group_names)})
        # print(group_names)
        # index = group_names.index("QA / Testing strategic group")
        # logger.info(f"{group_names[index]}")

        exclude_group_names = ['Ruby on Rails', 'Bluetooth Wi-Fi', 'Software Testing and QA ',
                               'nRoBo Test Automation Framework']

        # Iterate through all groups and repost to each of the group_name
        for idx, group_name in enumerate(group_names):

            # if idx < index:
            #     continue

            if group_name in exclude_group_names:
                continue  # skip share

            logger.info(f"idx={idx} groug-name={group_name}")
            post_settings_modal = select_a_group_modal.select_a_group_and_save(group_name)
            post_settings_modal.wait_for_a_while(Common.generate_random_numbers(2, 8))

            post_modal = post_settings_modal.post()
            post_modal = PagePostModal(post_modal.driver, post_modal.logger)
            post_modal.wait_for_a_while(Common.generate_random_numbers(3, 7))

            post_modal.write_thought(data['linkedin']['thought'])

            single_post_page = post_modal.post()
            single_post_page.wait_for_a_while(Common.generate_random_numbers(4, 6))

            repost_options = single_post_page.repost()
            repost_options.wait_for_a_while(Common.generate_random_numbers(2, 7))

            post_modal = repost_options.repost_with_your_thoughts()
            post_modal.wait_for_a_while(Common.generate_random_numbers(3, 5))

            post_settings_modal = post_modal.post_to_groups()
            post_settings_modal.wait_for_a_while(Common.generate_random_numbers(3, 5))

            select_a_group_modal = post_settings_modal.select_groups()
            select_a_group_modal.wait_for_a_while(Common.generate_random_numbers(3, 5))

    # @pytest.mark.run(order=2)
    @pytest.mark.linkedin
    def test_like_activity_posts(self, driver, logger):
        """Like all self activity posts"""

        cred = Common.read_yaml(cred_yaml_file)
        data = Common.read_yaml(test_data_yaml_file)

        page_home_public = PageHomePublic(driver, logger)
        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 5))
        page_home_public.maximize_window()
        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 3))
        page_home_public.get(data['linkedin']['linkedin_url'])

        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 6))
        page_home = page_home_public.login(cred['linkedin']['username'], cred['linkedin']['password'])

        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 5))
        page_all_recent_activity = page_home.open_all_activity_link(data['linkedin']['all_activity_url'])

        count = Common.read_yaml(counter_file)
        page_all_recent_activity.like_all_recent_posts(count[count_groups])

    @pytest.mark.youtube
    @pytest.mark.parametrize("username, password", youtube_users)
    def test_youtube_watch_nrobo_videos(self, driver, logger, username, password):
        """Watch YouTube Channel nRoBo Test Automation Framework"""

        page_gmail_login = PageGmailLogin(driver=driver, logger=logger)
        page_gmail_login.maximize_window()

        page_gmail_email_phone = page_gmail_login.open_gmail_login_url()

        page_gmail_email_phone.wait_for_a_while(2)

        logger.info(f"Enter email")
        page_gmail_email_phone.email_or_phone(username)
        page_gmail_password = page_gmail_email_phone.next()

        logger.info(f"Enter password")
        try:
            page_gmail_password.password(password)
            page_gmail_mailbox = page_gmail_password.next()
            page_youtube = page_gmail_mailbox.open_youtube_url()
            os.environ['channel_1'] = page_youtube.current_window_handle

            # open new window for Panchdev Singh Chauhan channel
            page_youtube.switch_to_new_window()
            page_youtube.maximize_window()
            page_youtube = page_gmail_mailbox.open_youtube_url()
            os.environ['channel_2'] = page_youtube.current_window_handle
        except Exception as e:
            pass

        os.environ['channel_1_searched'] = '0'
        os.environ['channel_2_searched'] = '0'
        # Infinite watching of nRoBo playlist
        watch_nrobo_playlist(driver, logger)


def watch_nrobo_playlist(driver, logger):
    """Watch nrobo playlist for infinite time"""

    channel_1 = channel_name_keyword_list[0][0]
    channel_1_keyword = channel_name_keyword_list[0][1]
    channel_2 = channel_name_keyword_list[1][0]
    channel_2_keyword = channel_name_keyword_list[1][1]
    channel_1_playlist = channel_1
    channel_2_playlist = playlist_list[0]
    os.environ['current_playlist'] = ""

    page_youtube_home_auth = PageYouTube(driver, logger)
    page_youtube_home_auth.wait_for_a_while(page_youtube_home_auth.generate_random_numbers(5, 7))

    if page_youtube_home_auth.current_window_handle == os.environ['channel_1'] \
            and int(os.environ['channel_1_searched']) == 0:
        page_playlists = page_youtube_home_auth.search(keyword=channel_1_keyword, channel_name=channel_1)
        page_playlists.click_link_view_full_playlist(channel_name=channel_1)
        os.environ['channel_1_searched'] = '1'

        page_watch_playlist = PageWatchPlaylist(driver, logger)

        page_watch_playlist.click_loop_playlist_button()
        page_watch_playlist.click_shuffle_playlist_button()

    elif page_youtube_home_auth.current_window_handle == os.environ['channel_2'] \
            and int(os.environ['channel_2_searched']) == 0:
        page_playlists = page_youtube_home_auth.search(
            keyword=channel_2_keyword,
            channel_name=channel_2,
            playlist_name=channel_2_playlist)
        # first playlist from list of playlists
        page_playlists.click_link_view_full_playlist(channel_name=channel_2)
        os.environ['channel_2_searched'] = '1'

        page_watch_playlist = PageWatchPlaylist(driver, logger)

        page_watch_playlist.click_loop_playlist_button()
        page_watch_playlist.click_shuffle_playlist_button()

    while True:
        try:
            page_watch_playlist.click_like_video()
            page_watch_playlist.click_volume_control_and_set_playback_speed_2x()
            from nrobo.util.common import Common
            page_watch_playlist.wait_for_a_while(Common.generate_random_numbers(25, 35))  # 25-35 min approx.
        except Exception as e:
            pass

        # switch channel
        if page_watch_playlist.current_window_handle == os.environ['channel_1'] \
                and not page_watch_playlist.current_playlist_matches(channel_1_playlist):
            os.environ['channel_1_searched'] = '0'
            page_watch_playlist.switch_to_window(os.environ['channel_1'])
            break
        elif page_watch_playlist.current_window_handle == os.environ['channel_2'] \
                and not page_watch_playlist.current_playlist_matches(channel_2_playlist):
            os.environ['channel_2_searched'] = '0'
            page_watch_playlist.switch_to_window(os.environ['channel_2'])
            break

        page_watch_playlist.refresh()
        page_watch_playlist.wait_for_page_to_be_loaded()

        page_watch_playlist.click_loop_playlist_button()
        page_watch_playlist.click_shuffle_playlist_button()

        # swap channel
        if page_youtube_home_auth.current_window_handle == os.environ['channel_1']:
            page_youtube_home_auth.switch_to_window(os.environ['channel_2'])
        elif page_youtube_home_auth.current_window_handle == os.environ['channel_2']:
            page_youtube_home_auth.switch_to_window(os.environ['channel_1'])

    watch_nrobo_playlist(driver, logger)  # Infinite call loop, needed though dangerous

