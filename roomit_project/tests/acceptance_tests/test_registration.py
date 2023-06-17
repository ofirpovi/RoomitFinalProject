import os
import django
from roomit_project.tests.acceptance_tests.roomit_base_tester import TestRoomit, generate_random_string
from parameterized import parameterized
from random import choice

# error messages
ERROR_PASSWORDS_DONT_MATCH = "The two password fields didn’t match."
ERROR_INVALID_USERNAME = "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters."
ERROR_PASSWORD_TOO_COMMON = "This password is too common."
ERROR_PASSWORD_ENTIRELY_NUMERIC = "This password is entirely numeric."
ERROR_PASSWORD_TOO_SHORT = "This password is too short. It must contain at least 8 characters."
ERROR_PASSWORD_SIMILAR_TO_USERNAME = "The password is too similar to the username."
ERROR_USERNAME_EXISTS = "A user with that username already exists."


class TestRegistration(TestRoomit):

    def test_registration(self):
        for name in self.names:
            self.click_register()
            # Profile information
            self.create_new_user(name, self.password)
            self.click_submit()
            self.profile_information(name)
            self.click_submit()

            if choice(self.bools):
                # Choose status
                self.click_link('For a property')

                # Property requirements
                self.property_requirements()
                self.click_submit()

            else:
                # Choose status
                self.click_link('For a roommate')

                # Property information
                self.property_information()
                self.click_submit()

            # Roommate requirements
            self.roommate_requirements()
            self.click_submit()

            # Logout
            self.click_logout()

    def test_register_when_already_logged_in_fail(self):
        self.login(self.username, self.password)
        self.check_logged_in_succeeded(self.username)

        # try to go back to register page
        self.driver.get(f"{self.base_url}user/register/")

        # todo - check he cant go back to login page or to register page
        self.check_logged_in_succeeded(self.username)

    def test_registration_username_exists_fail(self):
        name = generate_random_string(5)
        self.click_register()
        self.create_new_user(name, self.password, f"{name}1")
        self.click_submit()

        # Logout
        self.click_logout()
        self.click_register()
        self.create_new_user(name, self.password, f"{name}2")
        self.click_submit()

        self.assert_visible_text(ERROR_USERNAME_EXISTS, "error_1_id_username")
        self.assert_register_failed()

    def test_registration_invalid_username_fail(self):
        name = generate_random_string(5)
        self.click_register()
        self.create_new_user(f"{name}&", self.password, name)
        self.click_submit()

        self.assert_visible_text(ERROR_INVALID_USERNAME, "error_1_id_username")
        self.assert_register_failed()

    def test_registration_same_email_fail(self):
        name = generate_random_string(5)
        self.click_register()
        self.create_new_user(f"{name}1", self.password, email_name=name)
        self.click_submit()

        # Logout
        self.click_logout()
        self.click_register()
        self.create_new_user(f"{name}2", self.password, email_name=name)
        self.click_submit()

        self.assert_register_failed()

    @parameterized.expand([
        'password',
        'qwertyui',
        'abc12345',
        'admin123',
        'iloveyou',
        'welcome1',
        'pass1234',
        'changeme'
    ])
    def test_registration_common_password_fail(self, password):
        name = generate_random_string(5)
        self.click_register()
        self.create_new_user(name, password, name)
        self.click_submit()

        self.assert_visible_text(ERROR_PASSWORD_TOO_COMMON, "error_1_id_password2")
        self.assert_register_failed()

    def test_registration_short_password_fail(self):
        password = "a"
        name = generate_random_string(6)
        for i in range(1, 7):
            password = f"{password}{i}"

            self.click_register()
            self.create_new_user(name, password, name)
            self.click_submit()

            self.assert_visible_text(ERROR_PASSWORD_TOO_SHORT, "error_1_id_password2")
            self.assert_register_failed()
            self.click_register()

    def test_registration_numeric_password_fail(self):
        password = "620596532"
        name = generate_random_string(6)

        self.click_register()
        self.create_new_user(name, password, name)
        self.click_submit()

        self.assert_visible_text(ERROR_PASSWORD_ENTIRELY_NUMERIC, "error_1_id_password2")
        self.assert_register_failed()
        self.click_register()

    def test_registration_password_similar_to_username_fail(self):
        name = generate_random_string(6)
        password = f"{name}1234"

        self.click_register()
        self.create_new_user(name, password, name)
        self.click_submit()

        self.assert_visible_text(ERROR_PASSWORD_SIMILAR_TO_USERNAME, "error_1_id_password2")
        self.assert_register_failed()
        self.click_register()

    def test_registration_not_same_password_fail(self):
        name = generate_random_string(5)
        self.click_register()
        self.create_new_user(f"{name}", self.password, password2=f"{self.password}12")
        self.click_submit()

        self.assert_visible_text(ERROR_PASSWORDS_DONT_MATCH, "error_1_id_password2")
        self.assert_register_failed()

    def register_new_user(self, username, password):
        self.click_register()
        self.create_new_user(username, password)
        self.click_submit()

    def assert_register_failed(self):
        self.assert_element_by_id("id_username")
        self.assert_element_by_id("id_email")
        self.assert_element_by_id("id_password1")
        self.assert_element_by_id("id_password2")
        self.assert_visible_text_link("Login")
        self.assert_visible_text_link("Register")
