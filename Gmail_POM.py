# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 09:12:19 2018

@author: Tai
"""

from selenium import webdriver
from Util import logInfo, ReadExcel
from WebTools import browserSetup
import time

class Gmail_SigninUserID(object):
    
    def __init__(self, driver, userid):
        
        self.userid = userid
        #self.driver = driver
        self.userID = driver.find_element_by_id("identifierId")
        self.nextBtn = driver.find_element_by_xpath("//*[@id='identifierNext']/content/span") 
        print(self.userID, self.nextBtn)
        
    def submitUserID(self):
        
        logInfo("Gmail_SigninUserID : submitUserID()")
        self.userID.send_keys(self.userid)
        self.nextBtn.click()
        
        
class Gmail_SigninPassword(object):
    
    def __init__(self, driver, password):
        
        self.password = password
        #self.driver = driver
        self.passWORD = driver.find_element_by_name("password")
        self.nextBtn = driver.find_element_by_xpath("//*[@id='passwordNext']/content/span") 
        print(self.passWORD, self.nextBtn)
        
    def submitPassword(self):
        
        logInfo("Gmail_SigninPassword : submitPassword()")
        self.passWORD.send_keys(self.password)
        self.nextBtn.click()
        
class Gmail_Compose(object):
    
    def __init__(self, driver):
        
        self.driver = driver
        self.composeBtn = driver.find_element_by_xpath("//*[@id=':hd']/div/div")
        #print("composeBtn ======== ")
        #print(self.composeBtn)
        
        self.profilePic = driver.find_element_by_xpath("//*[@id=\"gb\"]/div[1]/div[1]/div/div[5]/div[1]/a/span")
        
    def sendEmail(self, mailto, subject, content):
        
        logInfo("Gmail_Compose : sendEmail()")
        self.composeBtn.click()
        time.sleep(10)
        
        # visible only after click()
        self.driver.find_element_by_name("to").send_keys(mailto)
        self.driver.find_element_by_name("subjectbox").send_keys(subject)
        self.driver.find_element_by_xpath("//*[@id=\":nk\"]").send_keys(content)
        self.driver.find_element_by_xpath("//*[@id=\":m5\"]").click()
        
        
    def logOut(self):
        
        logInfo("Gmail_Compose : logOut()")
        self.profilePic.click()
        time.sleep(3)
        
         # visible only after click()
        self.driver.find_element_by_link_text("Sign out").click()
        
        

def main():
    
    logInfo("Retrieve userid/password from excel")
    f = "C:\\2018\\edureka\\selenium\\INPUT\\gmail_input.xlsx"
    sh = ReadExcel(f, 'Sheet1')
    userid   = sh.get_data('A1') 
    password = sh.get_data('B1')
    logInfo("userid : " + userid + " password : " + password)
    
    driverPath = "C:\\2018\\Python\\selenium\\chromedriver.exe"
    url = "https://www.gmail.com/"
    driver = browserSetup(driverPath, url)
    
    g = Gmail_SigninUserID(driver, userid)
    g.submitUserID()
    
    logInfo("Sleep for few seconds")
    time.sleep(3)
    
    g1 = Gmail_SigninPassword(driver, password)
    g1.submitPassword()
    
    logInfo("Sleep for few seconds")
    time.sleep(10)
    
    mailto = "taislu@hotmail.com"
    subject = "Automated Gmail test"
    content = "This is an email sent via Selenium."
    
    c = Gmail_Compose(driver)
    c.sendEmail(mailto, subject, content)
    
    logInfo("Sleep for few seconds")
    time.sleep(3)
    
    c.logOut()
    logInfo("DONE!")


if __name__ == '__main__':
    main()