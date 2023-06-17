import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'roomit_project.settings'
django.setup()

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice, choices
from string import ascii_lowercase, digits
from django.test import TestCase


def generate_random_string(length):
    return ''.join(choices(ascii_lowercase + digits, k=length))


class TestRoomit(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:8000/"
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.names = [
            "Emma",
            "Liam",
            "Olivia",
            "Noah",
            "Ava",
            "Isabella",
            "Sophia",
            "Mia",
            "Charlotte",
            "Amelia",
            "Harper",
            "Evelyn",
            "Abigail",
            "Emily",
            "Elizabeth",
            "Mila",
            "Ella",
            "Avery",
            "Sofia",
            "Camila",
            "Aria",
            "Scarlett",
            "Victoria",
            "Madison",
            "Luna",
            "Grace",
            "Chloe",
            "Penelope",
            "Layla",
            "Riley",
            "Zoey",
            "Nora",
            "Lily",
            "Eleanor",
            "Hannah",
            "Lillian",
            "Addison",
            "Aubrey",
            "Ellie",
            "Stella",
            "Natalie",
            "Zoe",
            "Leah",
            "Hazel",
            "Violet",
            "Aurora",
            "Savannah",
            "Audrey",
            "Brooklyn",
            "Bella",
            "Claire"
        ]
        self.last_name = "Levi"
        self.counter = 5
        self.gender = [
            'F',
            'M',
            'T',
            'NB',
            'GN',
            "D"
        ]
        self.occupations = [
            'F',
            'S',
            'P',
            "D"
        ]
        self.smoker = [
            'Yes',
            'No',
            'Occasionally',
            'Socially',
            "D"
        ]
        self.diet = [
            'Carnivore',
            'Pescetarian',
            'Vegan',
            'Vegetarian',
            'Raw Veganism',
            "D"
        ]
        self.status = [
            'Single',
            'Married',
            'In a relationship',
            "D"
        ]
        self.hospitality = [
            'L',
            'N',
            "D"
        ]
        self.kosher = [
            'Y',
            'N',
            "D"
        ]
        self.expense_management = [
            'S',
            'I',
            "D"
        ]
        self.bools = [True, False]
        self.password = "sade12345"
        self.username = choice(self.names)
        self.login_url = f"{self.base_url}user/login/"

    def tearDown(self):
        self.driver.quit()

    # ----------------------------------------------------    ROOMIT ACTIONS   ----------------------------------------------------

    def click_register(self):
        self.driver.find_element(By.LINK_TEXT, "Register").click()

    def create_new_user(self, username, password1, email_name=None, password2=None):
        if email_name is None:
            email_name = username.lower()
        if password2 is None:
            password2 = password1
        self.driver.find_element(By.ID, "id_username").send_keys(username)
        self.driver.find_element(By.ID, "id_email").send_keys(f"{email_name}@gmail.com")
        self.driver.find_element(By.ID, "id_password1").send_keys(password1)
        self.driver.find_element(By.ID, "id_password2").send_keys(password2)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn"))).click()

    def login(self, username, password):
        self.driver.find_element(By.ID, "id_username").send_keys(username)
        self.driver.find_element(By.ID, "id_password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()

    def profile_information(self, name):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'id_first_name'))).send_keys(name)
        self.driver.find_element(By.ID, "id_last_name").send_keys(self.last_name)
        self.driver.find_element(By.ID, "id_birthdate").send_keys(f"01-01-{choice(range(1984, 2000))}")
        self.driver.find_element(By.ID, "id_phone_number").send_keys("+972521111111")
        self.select_dropdown_option("id_gender", self.gender)
        self.select_dropdown_option("id_occupation", self.occupations)
        self.select_dropdown_option("id_smoker", self.smoker)
        self.select_dropdown_option("id_diet", self.diet)
        self.select_dropdown_option("id_status", self.status)
        self.select_dropdown_option("id_hospitality", self.hospitality)
        self.select_dropdown_option("id_kosher", self.kosher)
        self.select_dropdown_option("id_expense_management", self.expense_management)

    def roommate_requirements(self):
        self.driver.find_element(By.ID, "id_Occupation").click()
        self.driver.find_element(By.ID, "id_MinAge").click()
        self.driver.find_element(By.ID, "id_MinAge").send_keys("25")
        self.driver.find_element(By.ID, "id_MaxAge").send_keys("40")
        self.select_dropdown_option("id_Gender", self.gender)
        self.select_dropdown_option("id_Smoker", self.smoker)
        self.select_dropdown_option("id_Diet", self.diet)
        self.select_dropdown_option("id_Kosher", self.kosher)
        self.select_dropdown_option("id_Status", self.status)
        self.select_dropdown_option("id_Expense_Management", self.expense_management)

    def property_information(self):
        roommates = choice(range(6)) + 1
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Draw a marker'))).click()
        self.driver.find_element(By.ID, "map").click()
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Draw a marker"))).click()
        self.driver.execute_script("window.scrollTo(0,33.599998474121094)")
        self.driver.find_element(By.ID, "id_rent").send_keys(roommates * 1000)
        self.driver.find_element(By.ID, "id_square_meters").send_keys(roommates * 20)
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_renovated > .form-check-label").click()
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_shelter_inside > .form-check-label").click()
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_shelter_nearby > .form-check-label").click()
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_furnished > .form-check-label").click()
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_shared_livingroom > .form-check-label").click()
        self.driver.find_element(By.ID, "id_rooms_number").send_keys(roommates + 1)
        self.driver.find_element(By.ID, "id_roomates_number").send_keys(roommates)
        self.driver.find_element(By.ID, "id_showers_number").send_keys(max(int(roommates/2), 1))
        self.driver.find_element(By.ID, "id_toilets_number").send_keys(max(int(roommates/2), 1))

    def property_requirements(self):
        roommates = choice(range(6))
        self.driver.find_element(By.LINK_TEXT, "Draw a rectangle").click()
        self.driver.find_element(By.ID, "map").click()
        self.driver.find_element(By.ID, "id_MinRent").send_keys(max((roommates * 1000) - 2000, 0))
        self.driver.find_element(By.ID, "id_MaxRent").send_keys((roommates * 1000) + 2000)
        self.driver.find_element(By.ID, "id_MinRooms").send_keys(max(roommates - 2, 1))
        self.driver.find_element(By.ID, "id_MaxRooms").send_keys(roommates + 2)
        self.driver.find_element(By.ID, "id_MaxRoommates").send_keys(roommates + 3)
        self.driver.find_element(By.ID, "id_MinRoommates").send_keys(max(roommates - 3, 1))
        self.driver.find_element(By.ID, "id_MinToilets").send_keys(max(int(roommates/2), 1))
        self.driver.find_element(By.ID, "id_MinShowers").send_keys(max(int(roommates/3), 1))
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_ShelterInside > .form-check-label").click()
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_ShelterNearby > .form-check-label").click()
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_Furnished > .form-check-label").click()
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_Renovated > .form-check-label").click()
        if choice(self.bools):
            self.driver.find_element(By.CSS_SELECTOR, "#div_id_SharedLivingRoom > .form-check-label").click()

    def like_unlike_user(self, username):
        self.wait.until((EC.visibility_of_element_located((By.XPATH, f"//*[@class='button' and @data-user='{username}']")))).click()

    def go_to_user_profile(self, username):
        self.driver.find_element(By.LINK_TEXT, f" More about {username} ").click()

    def like_unlike_from_profile(self, username):
        self.go_to_user_profile(username)
        self.like_unlike_user(username)

    # ------------------------------------------------------    VALIDATION   ----------------------------------------------------

    def check_logged_in_failed(self, username):
        # assert no elements of logged-in user appear
        assert self.wait.until(EC.invisibility_of_element_located((By.LINK_TEXT, f"ROOMIT - Hello {username}")))
        assert self.wait.until(EC.invisibility_of_element_located((By.LINK_TEXT, "Logout")))

        # assert elements of logged-out user still exist
        self.assert_visible_text_link("Login")
        assert self.wait.until(EC.visibility_of_element_located((By.ID, "id_username")))
        assert self.wait.until(EC.visibility_of_element_located((By.ID, "id_password")))

        # assert driver is still on login page
        assert self.current_url() == self.login_url

    def check_logged_in_succeeded(self, username):
        # assert no elements of logged-out user still exist
        assert self.wait.until(EC.invisibility_of_element_located((By.LINK_TEXT, "Login")))
        assert self.wait.until(EC.invisibility_of_element_located((By.ID, "id_username")))
        assert self.wait.until(EC.invisibility_of_element_located((By.ID, "id_password")))

        # assert elements of logged-in user appear
        self.assert_visible_text_link(f"ROOMIT - Hello {username}")
        self.assert_visible_text_link("Logout")

        # assert driver is on home page
        assert self.current_url() == self.base_url

    def check_like_succeeded(self, username):
        assert self.wait.until(EC.invisibility_of_element_located((By.XPATH, f"//*[@href='/like-picture/{username}/']")))
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@href='/unlike-picture/{username}/']")))

    def check_like_profile_succeeded(self, username):
        assert self.wait.until(EC.invisibility_of_element_located((By.XPATH, f"//*[@href='/like-profile/{username}/']")))
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@href='/unlike-profile/{username}/']")))

    def check_unlike_succeeded(self, username):
        assert self.wait.until(EC.invisibility_of_element_located((By.XPATH, f"//*[@href='/unlike-picture/{username}/']")))
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@href='/like-picture/{username}/']")))

    def check_unlike_profile_succeeded(self, username):
        assert self.wait.until(EC.invisibility_of_element_located((By.XPATH, f"//*[@href='/unlike-profile/{username}/']")))
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@href='/like-profile/{username}/']")))

    def check_like_failed(self, username):
        assert self.wait.until(EC.invisibility_of_element_located((By.XPATH, f"//*[@href='/unlike-picture/{username}/']")))
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@href='/like-picture/{username}/']")))

    def check_if_user_liked_me(self, username):
        self.click_link("Profile")
        self.click_link("Who Liked Me")
        self.assert_visible_text_link(username)

    def check_if_user_unliked_me(self, username):
        self.click_link("Profile")
        self.click_link("Who Liked Me")
        self.assert_invisible_text_link(username)

    def check_if_i_liked_user(self, username):
        self.click_link("Profile")
        self.click_link("Who I Liked")
        self.assert_visible_text_link(username)

    def check_if_i_unliked_user(self, username):
        self.click_link("Profile")
        self.click_link("Who I Liked")
        self.assert_invisible_text_link(username)

    # ----------------------------------------------------    SELENIUM ACTIONS   ----------------------------------------------------

    def select_dropdown_option(self, element_id, options):
        select = Select(self.driver.find_element(By.ID, element_id))
        select.select_by_value(choice(options))

    def assert_visible_text_link(self, text):
        assert self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))

    def assert_invisible_text_link(self, text):
        assert self.wait.until(EC.invisibility_of_element_located((By.LINK_TEXT, text)))

    def assert_visible_text(self, text, id):
        self.wait.until(EC.visibility_of_element_located((By.ID, id)))
        assert self.wait.until(EC.text_to_be_present_in_element(text_=text, locator=(By.ID, id)))

    def assert_element_by_id(self, id):
        assert self.wait.until(EC.visibility_of_element_located((By.ID, id)))

    def current_url(self):
        return self.driver.current_url

    def go_to_page(self, url):
        self.driver.get(url)

    def click_link(self, page):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, page))).click()
