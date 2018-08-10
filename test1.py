import time
from selenium import webdriver

#driver = webdriver.Firefox(executable_path="C:\\2018\\Python\\selenium\\geckodriver.exe")
driver = webdriver.Chrome(executable_path="C:\\2018\\Python\\selenium\\chromedriver.exe")
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!

driver.quit()

