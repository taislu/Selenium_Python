# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 08:56:51 2018

@author: Tai
"""
import time
from Util import ReadExcel, logInfo
from WebTools import browserSetup, browserClose
from Gmail_POM import Gmail_SigninUserID, Gmail_SigninPassword, Gmail_Compose

def signinGmail(driver, userid, password):
    
    logInfo("siginGmail() ")
    g = Gmail_SigninUserID(driver, userid)
    g.submitUserID()
    
    logInfo("Sleep for few seconds")
    time.sleep(3)
    
    g1 = Gmail_SigninPassword(driver, password)
    g1.submitPassword()

def composeGmail(driver, mailto, subject, content):
    
    c = Gmail_Compose(driver)
    c.sendEmail(mailto, subject, content)
    
    logInfo("Sleep for few seconds")
    time.sleep(3)
    
    c.logOut()
    
    
def getUserLogin():
    
    logInfo("initSetup()")
    
    logInfo("Retrieve userid/password from excel")
    f = "C:\\2018\\edureka\\selenium\\INPUT\\gmail_input.xlsx"
    sh = ReadExcel(f, 'Sheet1')
    userid   = sh.get_data('A1') 
    password = sh.get_data('B1')
    #logInfo("userid : " + userid + " password : " + password)
    
    return (userid, password)
    
def startChromeBrowser():
    
    driverPath = "C:\\2018\\Python\\selenium\\chromedriver.exe"
    url = "https://www.gmail.com/"
    driver = browserSetup(driverPath, url)
    
    return driver
    

def main():
    
    userdata = getUserLogin()
    print(userdata)

    driver = startChromeBrowser()
   
    logInfo("Test-1 : siginGmail() ")
    signinGmail(driver, userdata[0], userdata[1])
    
    logInfo("Sleep for few seconds")
    time.sleep(10)
    
    logInfo("Test-2 : composeGmail() and logOut() ")
    mailto = "taislu@hotmail.com"
    subject = "Automated Gmail test"
    content = "This is an email sent via Selenium."    
    composeGmail(driver, mailto, subject, content)
    
    browserClose(driver)
    logInfo("DONE!")

if __name__ == '__main__':
    main()