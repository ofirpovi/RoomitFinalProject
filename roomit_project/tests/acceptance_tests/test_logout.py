from telnetlib import EC
from selenium.webdriver.common.by import By
from roomit_project.tests.acceptance_tests.roomit_base_tester import TestRoomit, generate_random_string


class TestLogout(TestRoomit):
    def setUp(self):
        super().setUp()
        self.login(self.username, self.password)

    def tearDown(self):
         super().tearDown()

    def test_logout(self):
        self.click_logout()
        self.assert_logged_out()

    def assert_logged_out(self):
        self.assert_visible_text_link("Log In Again")
        assert self.wait.until(EC.text_to_be_present_in_element(text_="You have been loggedout", locator=(By.XPATH, "//*[@class='content-section w3-center']//*[text()='You have been loggedout']")))
        self.assert_visible_text_link("Login")
        self.assert_visible_text_link("Register")
        self.driver.get(f"http://127.0.0.1:8000/user/profile/{self.username}")
        assert self.current_url() == f"http://127.0.0.1:8000/user/login/?next=/user/profile/{self.username}/"
