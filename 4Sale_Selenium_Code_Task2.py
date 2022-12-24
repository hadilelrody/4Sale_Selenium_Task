#Libraries needed in this task
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

#This Function open the website i will work on
def get_website():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.saucedemo.com/')
    #This Function is used to slow down the proceeding to the next step to be able to see the result from each step
    sleep(2)
    return driver
  
#This Function Login to saucedemo website with valide credentials that are given in the website already
# and assert the proceeding to the next right page.
def login_using_valid_credntials(driver):
    username_element = driver.find_element(By.CSS_SELECTOR,'#user-name')
    password_element = driver.find_element(By.CSS_SELECTOR,'#password')
    submit_button_element = driver.find_element(By.CSS_SELECTOR,'#login-button')
    username_element.send_keys('standard_user')
    password_element.send_keys('secret_sauce')
    sleep(2)
    submit_button_element.click()
    sleep(2)
    assert "/inventory.html" in driver.current_url
    
#This Function sort the items and get the item with the lowest price first.
def lowest_price_item(driver):
    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_visible_text('Price (low to high)')
    sleep(2)
    
#This Function add the first item after sorting which is the lowest price item to the cart 
# then proceed to shopping cart page where item exists now and also assert the proceeding to the next right page.    
def add_to_cart(driver):
    add_to_cart_button_element = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
    add_to_cart_button_element.click()  
    sleep(3)
    shopping_cart_icon_element = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
    shopping_cart_icon_element.click()
    sleep(3)
    assert "/cart.html" in driver.current_url
    
#This Function proceed to checkout and assert the proceeding to the next right page.
def proceed_to_checkout(driver):
    checkout_button_element = driver.find_element(By.CSS_SELECTOR, '#checkout')
    checkout_button_element.click()  
    sleep(2)
    assert "/checkout-step-one.html" in driver.current_url
    
#This Function fills all the Personal data of the user to continue purchasing process
# and assert the proceeding to the next right page.
def fill_personal_data(driver):
    firstname_element = driver.find_element(By.CSS_SELECTOR,'#first-name')
    lastname_element = driver.find_element(By.CSS_SELECTOR,'#last-name')
    postalcode_element = driver.find_element(By.CSS_SELECTOR,'#postal-code')
    continue_button_element = driver.find_element(By.CSS_SELECTOR,'#continue')
    firstname_element.send_keys('Hadil')
    lastname_element.send_keys('Elrody')
    postalcode_element.send_keys('11865')
    sleep(2)
    continue_button_element.click()
    sleep(3)
    assert "/checkout-step-two.html" in driver.current_url
 
#This Function complete the checkout and assert the proceeding to the next right page.
def complete_checkout(driver):
    finish_button_element = driver.find_element(By.CSS_SELECTOR,'#finish')
    finish_button_element.click()
    sleep(2)
       
#This Function assert the proceeding to the page of completeing the checking out process & that the purchase is done.    
def assert_order_completed(driver):
    sleep(1000)
    assert "/checkout-complete.html" in driver.current_url
    
#This Function runs the whole sequence of purchasing step by step in form of calling functions in right order to achieve what we need.    
def whole_task_sequence():
    driver=get_website()
    login_using_valid_credntials(driver)
    lowest_price_item(driver)
    add_to_cart(driver)
    proceed_to_checkout(driver)
    fill_personal_data(driver)
    complete_checkout(driver)
    assert_order_completed(driver)
    sleep(100)
    
#The calling of the Function that contain the whole sequence that we need in this task       
whole_task_sequence()