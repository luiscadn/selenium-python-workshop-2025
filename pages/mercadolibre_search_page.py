from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MercadoLibrePage:
    SEARCH_FIELD = (By.NAME, 'as_word')  
    ELEMENTS_MSG = (By.XPATH, '/html/body/main/div/div[2]/section/div[7]/ol/li[1]/div/div/div/div[2]/h3/a')  

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        time.sleep(2) 
        search_input = self.driver.find_element(*self.SEARCH_FIELD)
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.ENTER)

    def verify_results(self, keyword):
        time.sleep(3)
        titles = self.driver.find_elements(*self.ELEMENTS_MSG)
        for title in titles:
            if keyword.lower() in title.text.lower():
                return True
        return False

