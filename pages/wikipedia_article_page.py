from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WikipediaArticlePage:
    ARTICLE_TITLE = (By.ID, "firstHeading")

    def __init__(self, driver):
        self.driver = driver

    def get_article_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ARTICLE_TITLE)
        )
        title_element = self.driver.find_element(*self.ARTICLE_TITLE)
        return title_element.text
