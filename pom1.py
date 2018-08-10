# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:17:06 2018

@author: Tai
"""

import time
from selenium import webdriver



class SignUp(object):
    
    def __init__(self, driver):
        self.driver = driver
    
    def FirstName(self, user_name):
        self.driver.find_element_by_name("firstname").clear()
        self.driver.find_element_by_name("firstname").send_keys(user_name)
        
    def LastName(self, password):
        self.driver.find_element_by_name("lastname").clear()
        self.driver.find_element_by_name("lastname").send_keys(password)
        
driver = webdriver.Chrome(executable_path="C:\\2018\\Python\\selenium\\chromedriver.exe")
driver.get("https:www.facebook.com")

signup = SignUp(driver)
signup.FirstName("Hello")
signup.LastName("World")
time.sleep(5)

driver.quit()