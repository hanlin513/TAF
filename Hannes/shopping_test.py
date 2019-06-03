from Main_Page import Main_Page
import unittest
from selenium import webdriver
import time


class ShoppingTest(unittest.TestCase):

    driver =""
    main_page = ""
    first_item_index = 0

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")   
        self.driver.get('http://automationpractice.com')
        self.main_page = Main_Page(self.driver)
        ##assert self.main_page.get_no_of_items_in_cart() == 0

    def testAddFirstItemToCartFromSearch(self):
        search_results = self.main_page.search("dress")
        search_results.add_item_to_cart(self.first_item_index)
        assert self.main_page.get_no_of_items_in_cart() == 1

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()