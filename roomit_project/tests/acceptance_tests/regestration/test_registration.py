import os
import django
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

os.environ['DJANGO_SETTINGS_MODULE'] = 'roomit_project.settings'
django.setup()

from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random import choice

class TestRegistration(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/user/login/?next=/")
        self.driver.maximize_window()
        self.vars = {}
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
        self.wait = WebDriverWait(self.driver, 10)
        self.bools = [True, False]

    def tearDown(self):
        self.driver.quit()

    def select_dropdown_option(self, element_id, options):
        select = Select(self.driver.find_element(By.ID, element_id))
        select.select_by_value(choice(options))


    def test_registration(self):
        # while True:
        #     self.driver.find_element(By.LINK_TEXT, "Register").click()
        #     name = self.names[self.counter]
        #     self.create_new_user(name)
        #     self.click_submit()
        #     try:
        #         self.wait.until(EC.visibility_of_element_located((By.ID, "error_1_id_username")))
        #         self.counter += 1
        #     except:
        #         break
        #

        for name in self.names:
            self.driver.find_element(By.LINK_TEXT, "Register").click()
            self.create_new_user(name)
            self.click_submit()


            # Profile information
            self.profile_information(name)
            self.click_submit()

            if choice(self.bools):
                # Choose status
                self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'For a property'))).click()

                # Property requirements
                self.property_requirements()
                self.click_submit()

            else:
                # Choose status
                self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'For a roommate'))).click()

                # Property information
                self.property_information()
                self.click_submit()

            # Roommate requirements
            self.roommate_requirements()
            self.click_submit()

            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()

    def profile_information(self, name):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'id_first_name'))).send_keys(name)
        self.driver.find_element(By.ID, "id_last_name").send_keys(self.last_name)
        # self.driver.find_element(By.ID, "id_birthdate").send_keys("01-01-1991")
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

    def create_new_user(self, name):
        self.driver.find_element(By.ID, "id_username").send_keys(name)
        self.driver.find_element(By.ID, "id_email").send_keys(f"{name.lower()}@gmail.com")
        self.driver.find_element(By.ID, "id_password1").send_keys("sade12345")
        self.driver.find_element(By.ID, "id_password2").send_keys("sade12345")

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

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

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

