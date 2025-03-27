import time

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class Test_Pom(WebDriverSetup):

    def test_add_item(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.sign_up('luiggi','luiggi@test.com', '8293998662')
        time.sleep(3)
