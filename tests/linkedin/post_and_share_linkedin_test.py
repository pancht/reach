import pytest

from pages.LinkedIn.auth.home.post_modal import PagePostModal
from pages.LinkedIn.auth.home.single_post import PageSinglePost
from pages.LinkedIn.public.PageHomePublic import PageHomePublic
from nrobo.util.common import Common

counter_file = "Counter.yaml"
count_groups = "count_groups"


class TestPostAndShareNRoBoUpdates:

    # @pytest.mark.run(order=1)
    def test_post_and_share_nrobo_updates_linkedin(self, driver, logger):
        """Post and share nRoBo updates on LinkedIn"""

        cred = Common.read_yaml('cred.yaml')
        data = Common.read_yaml('test_data.yaml')

        page_home_public = PageHomePublic(driver, logger)
        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 5))
        page_home_public.maximize_window()
        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 3))
        page_home_public.get(data['linkedin_url'])

        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 6))
        page_home = page_home_public.login(cred['username'], cred['password'])

        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 5))
        page_single_post = page_home.open_post_link(data['post_url'])

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

        exclude_group_names = ['Ruby on Rails', 'Bluetooth Wi-Fi', 'Software Testing and QA ']

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

            post_modal.write_thought(data['thought'])

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
    def test_like_activity_posts(self, driver, logger):
        """Like all self activity posts"""

        cred = Common.read_yaml('cred.yaml')
        data = Common.read_yaml('test_data.yaml')

        page_home_public = PageHomePublic(driver, logger)
        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 5))
        page_home_public.maximize_window()
        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 3))
        page_home_public.get(data['linkedin_url'])

        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 6))
        page_home = page_home_public.login(cred['username'], cred['password'])

        page_home_public.wait_for_a_while(Common.generate_random_numbers(2, 5))
        page_all_recent_activity = page_home.open_all_activity_link(data['all_activity_url'])

        count = Common.read_yaml(counter_file)
        page_all_recent_activity.like_all_recent_posts(count[count_groups])
