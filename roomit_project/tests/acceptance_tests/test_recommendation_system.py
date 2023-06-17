from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from roomit_project.tests.acceptance_tests.roomit_base_tester import TestRoomit, generate_random_string
from selenium.webdriver.support import expected_conditions as EC


class TestRecommendationSystem(TestRoomit):
    def setUp(self):
        super().setUp()
        self.rec_user1 = generate_random_string(6)
        self.rec_user2 = generate_random_string(6)
        self.click_register()
        self.create_new_user(self.rec_user1, self.password)
        self.click_submit()

        self.profile_information(self.rec_user1)
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

        self.click_register()
        self.create_new_user(self.rec_user2, self.password)
        self.click_submit()
        self.profile_information(self.rec_user2)
        self.click_submit()

        # Choose status
        self.click_link('For a property')

        # Property information
        self.property_requirements()
        self.click_submit()

        # Roommate requirements
        self.roommate_requirements()
        self.click_submit()

        self.click_link("Home")

    def tearDown(self):
        super().tearDown()

    def test_recommendation_system(self):
        self.go_to_page(self.base_url)
        like_element = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/a[2]')))
        href = like_element.get_attribute("href")
        user_liked = href[35:-1]
        like_element.click()
        self.click_logout()

        self.click_link("Login")
        self.login(self.rec_user1, self.password)
        like_element = self.wait.until(EC.presence_of_element_located((By.XPATH,f"//*[@class='w3-container']//a[@href='user/profile/{user_liked}']")))
        like_element.click()
        self.like_unlike_user(user_liked)
        self.go_to_page(self.base_url)
        self.wait.until(EC.invisibility_of_element((By.XPATH,f"//*[@class='w3-container']//a[@href='user/profile/{user_liked}']")))
        self.like_unlike_user(user_liked)
        self.click_logout()

        self.click_link("Login")
        self.login(self.rec_user2, self.password)
        self.wait.until(EC.invisibility_of_element((By.XPATH,f"//*[@class='w3-container']//a[@href='user/profile/{user_liked}']")))
        self.like_unlike_user(user_liked)
        self.wait.until(EC.presence_of_element_located((By.XPATH,f"//*[@class='w3-container']//a[@href='user/profile/{user_liked}']")))
        self.like_unlike_user(user_liked)
        self.click_logout()

    def select_dropdown_option(self, element_id, options):
        select = Select(self.driver.find_element(By.ID, element_id))
        select.select_by_value(options[0])
