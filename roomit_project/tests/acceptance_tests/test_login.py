import os
import django
from roomit_project.tests.acceptance_tests.roomit_base_tester import TestRoomit, generate_random_string


class TestLogin(TestRoomit):
    def setUp(self):
        super().setUp()
        self.driver.get(self.login_url)

    def tearDown(self):
        super().tearDown()

    def test_login_success(self):
        self.login(self.username, self.password)
        self.check_logged_in_succeeded(self.username)
        self.click_logout()

    def test_login_wrong_password_fail(self):
        self.login(self.username, generate_random_string(10))
        self.check_logged_in_failed(self.username)

    def test_login_wrong_username_fail(self):
        # add num to the end of the username
        self.login(f"{self.username}1", self.password)
        self.check_logged_in_failed(f"{self.username}1")
        self.check_logged_in_failed(self.username)
        self.driver.get(self.login_url)

        # add num to the beginning of the username
        self.login(f"1{self.username}", self.password)
        self.check_logged_in_failed(f"1{self.username}")
        self.check_logged_in_failed(self.username)
        self.driver.get(self.login_url)

        # same username lowercase
        self.login(self.username.lower(), self.password)
        self.check_logged_in_failed(self.username.lower())
        self.check_logged_in_failed(self.username)
        self.driver.get(self.login_url)

        # same username uppercase
        self.login(self.username.upper(), self.password)
        self.check_logged_in_failed(self.username.upper())
        self.check_logged_in_failed(self.username)

    def test_login_user_doesnt_exist_fail(self):
        # add num to the end of the username
        username = generate_random_string(8)
        self.login(username, self.password)
        self.check_logged_in_failed(username)
        self.driver.get(self.login_url)

    def test_login_when_already_logged_in_fail(self):
        self.login(self.username, self.password)
        self.check_logged_in_succeeded(self.username)

        # try to go back to login page
        self.driver.get(self.login_url)

        # todo - check he cant go back to login page or to register page
        self.check_logged_in_succeeded(self.username)

    def test_register_when_already_logged_in_fail(self):
        self.login(self.username, self.password)
        self.check_logged_in_succeeded(self.username)

        # try to go back to register page
        self.driver.get(f"{self.base_url}user/register/")

        # todo - check he cant go back to login page or to register page
        self.check_logged_in_succeeded(self.username)
