import requests, json,sys
import unittest,os,time
from datetime import datetime
from colorama import *
from selenium import webdriver

import unittest,os,time
from selenium import webdriver
os.environ["SELENIUM_SERVER_JAR"] = "/usr/local/bin/selenium-server-standalone-2.52.0.jar"
path=os.getcwd() + '/IEDriverServer'
chrome_driver_path = os.getcwd() + "/chromedriver"
opera_path=os.getcwd() + "/operadriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get('https://www.mapdevelopers.com/distance_from_to.php')
driver.find_element_by_name('from').send_keys()
driver.find_element_by_name('')