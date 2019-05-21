from selenium import webdriver
from Search_Results import Search_Results

class Main_Page:
    
    def __init__(self, driver):
        self.driver = driver

    def search(self, keyword):
        # find the search bar
        inputElement = self.driver.find_element_by_id("search_query_top")
        # search for a dress
        inputElement.send_keys(keyword)
        # submit search
        inputElement = self.driver.find_element_by_name("submit_search").click()
        return Search_Results(self.driver)

    def get_no_of_items_in_cart(self):
        cart_items = self.driver.find_element_by_class_name("ajax_cart_quantity")
        no_of_items = cart_items.get_attribute("innerHTML")
        if no_of_items == "empty":
            return 0
        else:
            return int(cart_items.get_attribute("innerHTML"))