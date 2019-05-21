import unittest
from selenium import webdriver
import time

class ShoppingTest(unittest.TestCase):

    def driver

    def setUp(self):
        self.driver = webdriver.Chrome()   
        self.driver.get('http://automationpractice.com')

    def testAddItemToCartFromSearch(self):
        
        # find the search bar
        inputElement = self.driver.find_element_by_id("search_query_top")

        # search for a dress
        inputElement.send_keys("dress")

        # submit search
        inputElement = self.driver.find_element_by_name("submit_search").click()
                
        # add first item to cart
        item_list = self.driver.find_element_by_css_selector(".product_list.grid.row")
        items = item_list.find_elements_by_class_name("product-container")
        items[0].find_element_by_css_selector(".button.ajax_add_to_cart_button").click()

        #Find no of items in shopping cart
        cart_items = self.driver.find_element_by_class_name("ajax_cart_quantity")
        assert cart_items.get_attribute("innerHTML") == "1"
        print("Test passed")

if __name__ == "__main__":
    unittest.main()