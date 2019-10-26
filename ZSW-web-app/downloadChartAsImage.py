import sys
import time
from selenium import webdriver
from requests import get

ip = get('https://api.ipify.org').text
driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://" + ip +":5000/")
button = driver.find_element_by_id(sys.argv[1]+"-chart").find_elements_by_class_name("modebar-btn")[0]
driver.execute_script("arguments[0].click();", button)
time.sleep(2)
driver.close()

