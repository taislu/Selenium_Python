# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 08:27:14 2018

@author: Tai
"""

from selenium import webdriver
from Util import logInfo


def browserSetup(driverPath, url):
    
    logInfo("browserSetup()")
    
    logInfo("Start Chrome webdriver")
    driver = webdriver.Chrome(executable_path=driverPath)
    
    logInfo("Set Page load timeout 30 sec")
    driver.set_page_load_timeout(30)
    
    logInfo("Set Implicitly Wait timeout 15 sec")
    driver.implicitly_wait(15)
    
    logInfo("Navigate to URL : " + url)
    driver.get(url)
    
    logInfo("Maximize Window")
    driver.maximize_window()

    return driver

def browserClose(driver):
    
    logInfo("browserClose()")
    
    logInfo("Close browser")
    driver.close()
    

def main():
    
    driverPath = "C:\\2018\\Python\\selenium\\chromedriver.exe"
    url = "https://www.gmail.com/"
    driver = browserSetup(driverPath, url)
    browserClose(driver)


if __name__ == '__main__':
    main()