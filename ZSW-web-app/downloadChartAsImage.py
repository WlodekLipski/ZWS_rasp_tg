import sys
import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://156.17.169.251:5000/")
button = driver.find_element_by_id(sys.argv[1]+"-chart").find_elements_by_class_name("modebar-btn")[0]
driver.execute_script("arguments[0].click();", button)
time.sleep(2)
driver.close()