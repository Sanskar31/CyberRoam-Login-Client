from selenium import webdriver
from secret import pw
from time import sleep
from selenium.webdriver.common.keys import Keys
from secret import username
from numpy import *

def __init__(self, username, pw):
    self.driver = webdriver.Firefox()
    self.driver.get("http://172.16.1.1:8090/")
    self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(username)
    self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(pw)
    self.driver.find_element_by_xpath('//input[@id="logincaption"]')\
        .click()
    #py.hotkey('ctrl', 't')
    
    self.driver.execute_script("window.open('http://fast.com', 'new_window')")
    #self.driver.switch_to_window(driver.window_handles[0])
    self.driver.execute_script("window.open('http://fast.com', 'new_window')")
    #py.hotkey('ctrl', 'tab')
    sleep(5)
    while(1):
        self.driver.find_element_by_xpath('//input[@id="logincaption"]')\
            .click()
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//input[@id="logincaption"]')\
            .click()
        sleep(5)