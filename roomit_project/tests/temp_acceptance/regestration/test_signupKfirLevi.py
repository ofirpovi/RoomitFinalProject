# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSignupKfirLevi():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_signupKfirLevi(self):
    self.driver.get("http://127.0.0.1:8000/user/login/?next=/")
    self.driver.set_window_size(784, 816)
    self.driver.find_element(By.LINK_TEXT, "Sign Up Now").click()
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("Kfir")
    self.driver.find_element(By.ID, "id_email").send_keys("kfir@gmail.com")
    self.driver.find_element(By.ID, "id_password1").send_keys("sade12345")
    self.driver.find_element(By.ID, "id_password2").send_keys("sade12345")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "id_first_name").click()
    self.driver.find_element(By.ID, "id_first_name").send_keys("Kfir")
    self.driver.find_element(By.ID, "id_last_name").click()
    self.driver.find_element(By.ID, "id_last_name").send_keys("Levi")
    self.driver.find_element(By.ID, "id_birthdate").click()
    self.driver.find_element(By.ID, "id_birthdate").send_keys("1999-03-12")
    self.driver.find_element(By.ID, "id_phone_number").send_keys("+12125552368")
    self.driver.find_element(By.ID, "id_gender").click()
    dropdown = self.driver.find_element(By.ID, "id_gender")
    dropdown.find_element(By.XPATH, "//option[. = 'Male']").click()
    self.driver.find_element(By.ID, "id_about_me").click()
    self.driver.find_element(By.ID, "id_about_me").send_keys("hello")
    self.driver.find_element(By.ID, "id_occupation").click()
    dropdown = self.driver.find_element(By.ID, "id_occupation")
    dropdown.find_element(By.XPATH, "//option[. = 'Student']").click()
    self.driver.find_element(By.ID, "id_smoker").click()
    dropdown = self.driver.find_element(By.ID, "id_smoker")
    dropdown.find_element(By.XPATH, "//option[. = 'No']").click()
    self.driver.find_element(By.ID, "id_diet").click()
    dropdown = self.driver.find_element(By.ID, "id_diet")
    dropdown.find_element(By.XPATH, "//option[. = 'Vegan']").click()
    self.driver.find_element(By.ID, "id_status").click()
    dropdown = self.driver.find_element(By.ID, "id_status")
    dropdown.find_element(By.XPATH, "//option[. = 'Single']").click()
    self.driver.find_element(By.ID, "div_id_hospitality").click()
    self.driver.find_element(By.ID, "id_hospitality").click()
    dropdown = self.driver.find_element(By.ID, "id_hospitality")
    dropdown.find_element(By.XPATH, "//option[. = 'Prefer not']").click()
    self.driver.find_element(By.ID, "id_kosher").click()
    dropdown = self.driver.find_element(By.ID, "id_kosher")
    dropdown.find_element(By.XPATH, "//option[. = 'Yes']").click()
    self.driver.find_element(By.ID, "id_expense_management").click()
    dropdown = self.driver.find_element(By.ID, "id_expense_management")
    dropdown.find_element(By.XPATH, "//option[. = 'Prefer not']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-info").click()
    self.driver.find_element(By.LINK_TEXT, "Looking for a property").click()
    self.driver.find_element(By.ID, "id_Country").send_keys("Israel")
    self.driver.find_element(By.ID, "id_City").send_keys("Tel aviv")
    self.driver.find_element(By.ID, "id_Neighborhood").send_keys("center")
    self.driver.find_element(By.ID, "id_MinRent").send_keys("5000")
    self.driver.find_element(By.ID, "id_MaxRent").send_keys("6000")
    self.driver.find_element(By.ID, "id_MinRooms").send_keys("3")
    self.driver.find_element(By.ID, "id_MaxRooms").send_keys("5")
    self.driver.find_element(By.ID, "id_MaxRoommates").send_keys("4")
    self.driver.find_element(By.ID, "id_MinRoommates").send_keys("2")
    self.driver.find_element(By.ID, "id_MinToilets").send_keys("2")
    self.driver.find_element(By.ID, "id_MinShowers").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "#div_id_ShelterInside > .form-check-label").click()
    self.driver.find_element(By.CSS_SELECTOR, "#div_id_Furnished > .form-check-label").click()
    self.driver.find_element(By.CSS_SELECTOR, "#div_id_Renovated > .form-check-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-info").click()
    dropdown = self.driver.find_element(By.ID, "id_Occupation")
    dropdown.find_element(By.XPATH, "//option[. = 'Full-time job']").click()
    self.driver.find_element(By.ID, "id_MinAge").send_keys("20")
    self.driver.find_element(By.ID, "id_MaxAge").send_keys("30")
    self.driver.find_element(By.ID, "id_Gender").click()
    dropdown = self.driver.find_element(By.ID, "id_Gender")
    dropdown.find_element(By.XPATH, "//option[. = 'Female']").click()
    self.driver.find_element(By.ID, "id_Smoker").click()
    dropdown = self.driver.find_element(By.ID, "id_Smoker")
    dropdown.find_element(By.XPATH, "//option[. = 'No']").click()
    self.driver.find_element(By.ID, "id_Diet").click()
    dropdown = self.driver.find_element(By.ID, "id_Diet")
    dropdown.find_element(By.XPATH, "//option[. = 'Carnivore']").click()
    self.driver.find_element(By.ID, "id_Kosher").click()
    dropdown = self.driver.find_element(By.ID, "id_Kosher")
    dropdown.find_element(By.XPATH, "//option[. = 'Yes']").click()
    self.driver.find_element(By.ID, "id_Status").click()
    dropdown = self.driver.find_element(By.ID, "id_Status")
    dropdown.find_element(By.XPATH, "//option[. = 'Single']").click()
    self.driver.find_element(By.ID, "id_Expense_Management").click()
    dropdown = self.driver.find_element(By.ID, "id_Expense_Management")
    dropdown.find_element(By.XPATH, "//option[. = 'Love']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-info").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-info").click()
    self.driver.close()

