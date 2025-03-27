from selenium.webdriver.common.by import By
import time

base_url = 'https://testautomationpractice.blogspot.com/'


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.name = 'name'
        self.email = 'email'
        self.phone = 'phone'
        self.wikipedia_search = '//*[@id="Wikipedia1_wikipedia-search-input"]'
        self.address_textarea = '//*[@id="textarea"]'
        self.gender_male = '//*[@id="male"]'
        self.gender_female = '//*[@id="female"]'

    def get_name(self):
        return self.driver.find_element(By.ID, 'name')

    def get_email(self):
        return self.driver.find_element(By.ID, 'email')

    def get_phone(self):
        return self.driver.find_element(By.ID, 'phone')

    def get_wikipedia(self):
        return self.driver.find_element(By.ID, self.wikipedia_search)

    def get_address(self):
        return self.driver.find_element(By.ID, self.address_textarea)

    def get_gender_male(self):
        return self.driver.find_element(By.ID, self.gender_male)

    def get_gender_female(self):
        return self.driver.find_element(By.ID, self.gender_female)

    def sign_up(self, name, email, phone):
        self.get_name().send_keys(name)
        self.get_email().send_keys(email)
        self.get_phone().send_keys(phone)
        time.sleep(3)

    @staticmethod
    def get_base_url():
        return base_url
