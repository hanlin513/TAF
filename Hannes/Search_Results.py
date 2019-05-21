from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Search_Results:
    timeout = 10
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, index):
        item_list = self.driver.find_element_by_css_selector(".product_list.grid.row")
        items = item_list.find_elements_by_class_name("product-container")
        items[index].find_element_by_css_selector(".button.ajax_add_to_cart_button").click()
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "icon-ok")))
        except:
            self.driver.quit()
