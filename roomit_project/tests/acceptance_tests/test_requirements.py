from telnetlib import EC

from selenium.webdriver.common.by import By

from roomit_project.tests.acceptance_tests.roomit_base_tester import TestRoomit, generate_random_string


class TestRequirements(TestRoomit):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_property_reqs_offline_fail(self):
        self.go_to_page(f"{self.base_url}user/property-reqs-display/{self.username}/")
        assert self.current_url() == f"{self.base_url}user/login/?next=/user/property-reqs-display/{self.username}/"

    def test_roomi_reqs_offline_fail(self):
        self.go_to_page(f"{self.base_url}user/roomi-reqs-display/{self.username}/")
        assert self.current_url() == f"{self.base_url}user/login/?next=/user/roomi-reqs-display/{self.username}/"

    def test_property_offer_offline_fail(self):
        self.go_to_page(f"{self.base_url}user/property-offer-display/{self.username}/")
        assert self.current_url() == f"{self.base_url}user/login/?next=/user/property-offer-display/{self.username}/"

    def test_profile_info_offline_fail(self):
        self.go_to_page(f"{self.base_url}user/profile/{self.username}/")
        assert self.current_url() == f"{self.base_url}user/login/?next=/user/profile/{self.username}/"

    def test_change_requirements_success(self):
        self.click_link("Login")
        self.login(self.username, self.password)

        self.click_link("Profile")
        self.profile_information(self.username)
        self.click_submit()

        self.driver.find_element(By.CSS_SELECTOR, ".w3-hover-none").click()
        self.click_link("On Property")
        self.property_requirements()
        self.click_submit()

        self.driver.find_element(By.CSS_SELECTOR, ".w3-hover-none").click()
        self.click_link("On Roommate")
        self.roommate_requirements()
        self.click_submit()
