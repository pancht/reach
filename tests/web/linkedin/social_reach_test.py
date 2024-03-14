import pytest
from nrobo.util.common import Common

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

youtube_test_data = Common.read_yaml(cred_yaml_file)['youtube']
youtube_users = [(cred['username'], cred['password']) for cred in youtube_test_data]


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

        # Common.write_yaml(counter_file, {count_groups: len(group_names)})
        # print(group_names)
        # index = group_names.index("Penetration Testing / Ethical Hacking")
        # logger.info(f"{group_names[index]}")

        exclude_group_names = ['Ruby on Rails', 'Bluetooth Wi-Fi', 'Software Testing and QA ', 'nRoBo Test Automation Framework']

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
        page_gmail_password.password(password)
        page_gmail_mailbox = page_gmail_password.next()
        page_youtube = page_gmail_mailbox.open_youtube_url()

        # Infinite watching of nRoBo playlist
        watch_nrobo_playlist(page_youtube.driver, page_youtube.logger)


def watch_nrobo_playlist(driver, logger):
    """Watch nrobo playlist for infinite time"""

    page_youtube = PageYouTube(driver, logger)
    page_playlists = page_youtube.search("nrobo")
    page_playlists.click_link_view_nrobo_full_playlist()

    # page_watch_playlist = page_playlists.click_play_all()
    page_watch_playlist = PageWatchPlaylist(page_playlists.driver, page_playlists.logger)

    page_watch_playlist.click_loop_playlist_button()
    page_watch_playlist.click_shuffle_playlist_button()

    while True:
        page_watch_playlist.click_like_video()
        page_watch_playlist.click_volume_control_and_set_playback_speed_2x()
        page_watch_playlist.wait_for_a_while(10 * 60)

        if not page_watch_playlist.current_playlist_is_nrobo():
            break

        page_watch_playlist.refresh()
        page_watch_playlist.click_loop_playlist_button()
        page_watch_playlist.click_shuffle_playlist_button()

    watch_nrobo_playlist(driver, logger)  # Infinite call loop, needed though dangerous










