from selenium import webdriver
import time

driver = webdriver.Chrome()   
driver.get('http://automationpractice.com')
# find the search bar
inputElement = driver.find_element_by_id("search_query_top")

# search for a dress
inputElement.send_keys("dress")

# submit search
inputElement = driver.find_element_by_name("submit_search").click()

        
# add first item to cart
item_list = driver.find_element_by_css_selector(".product_list.grid.row")
items = item_list.find_elements_by_class_name("product-container")
items[0].find_element_by_css_selector(".button.ajax_add_to_cart_button").click()

#Ugly wait for shopping cart to update
time.sleep(3)

 #Find no of items in shopping cart
cart_items = driver.find_element_by_class_name("ajax_cart_quantity")
assert cart_items.get_attribute("innerHTML") == "1"
print("Test passed")
