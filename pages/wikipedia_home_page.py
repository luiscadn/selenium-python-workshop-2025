from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WikipediaHomePage:
    SEARCH_INPUT = (By.NAME, "search")

    def __init__(self, driver):
        self.driver = driver

    def search_article(self, article_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_field = self.driver.find_element(*self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(article_name)
        search_field.send_keys(Keys.ENTER) 
