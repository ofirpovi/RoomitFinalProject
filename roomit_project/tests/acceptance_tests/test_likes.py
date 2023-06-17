from roomit_project.tests.acceptance_tests.roomit_base_tester import TestRoomit, generate_random_string

class TestLikeuser(TestRoomit):
    def setUp(self):
        super().setUp()
        # self.login_url = f"{self.base_url}user/login/"
        self.name1 = generate_random_string(6)

        self.click_register()
        self.create_new_user(self.name1, self.password)
        self.click_submit()

        self.profile_information(self.name1)
        self.click_submit()

        # Choose status
        self.click_link('For a property')

        # Property requirements
        self.property_requirements()
        self.click_submit()

        # Roommate requirements
        self.roommate_requirements()
        self.click_submit()

        # Logout
        self.click_logout()

        self.name2 = generate_random_string(6)
        self.click_register()
        self.create_new_user(self.name2, self.password)
        self.click_submit()

        self.profile_information(self.name2)
        self.click_submit()

        # Choose status
        self.click_link('For a roommate')

        # Property information
        self.property_information()
        self.click_submit()

        # Roommate requirements
        self.roommate_requirements()
        self.click_submit()

    def tearDown(self):
        self.click_logout()
        super().tearDown()
  
    def test_like_unlike_user(self):
        self.like_unlike_user(self.name1)
        self.check_like_succeeded(self.name1)
        self.check_if_i_liked_user(self.name1)
        self.click_logout()
        self.login(self.name1, self.password)
        self.check_if_user_liked_me(self.name2)
        self.click_logout()

        self.login(self.name2, self.password)
        self.like_unlike_user(self.name1)
        self.check_unlike_succeeded(self.name1)
        self.check_if_i_unliked_user(self.name1)
        self.click_logout()
        self.login(self.name1, self.password)
        self.check_if_user_unliked_me(self.name2)

    def test_like_unlike_from_profile(self):
        self.like_unlike_from_profile(self.name1)
        self.check_like_profile_succeeded(self.name1)
        self.check_if_i_liked_user(self.name1)
        self.click_logout()
        self.login(self.name1, self.password)
        self.check_if_user_liked_me(self.name2)
        self.click_logout()

        self.login(self.name2, self.password)
        self.like_unlike_from_profile(self.name1)
        self.check_unlike_profile_succeeded(self.name1)
        self.check_if_i_unliked_user(self.name1)
        self.click_logout()
        self.login(self.name1, self.password)
        self.check_if_user_unliked_me(self.name2)

    def test_check_who_liked_me_no_user_logged_in_fail(self):
        self.click_logout()
        self.driver.get(f"{self.base_url}likes-me/")
        assert self.current_url() == f"{self.base_url}user/login/?next=/likes-me/"

    def test_check_who_i_liked_no_user_logged_in_fail(self):
        self.click_logout()
        self.driver.get(f"{self.base_url}i-like/")
        assert self.current_url() == f"{self.base_url}user/login/?next=/i-like/"
