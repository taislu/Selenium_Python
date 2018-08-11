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

"""
http://selenium-python.readthedocs.io/locating-elements.html

find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
"""