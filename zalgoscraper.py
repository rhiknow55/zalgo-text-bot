# For the scraping
# import requests
# import urllib.request
import time
# from bs4 import BeautifulSoup # a tool for parsing json and xml

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()


url = "https://www.zalgotextgenerator.com/"
# url = "https://lingojam.com/ZalgoText"
# url = "https://www.piliapp.com/cool-text/zalgo-text/"
# This should return 200 to show that we can access the url with our requests library
# response = requests.get(url)
driver.get(url)


# Pass in the message to convert as parameter
# Then query the converter website using a selenium web driver
def scrapeWebsite(message):

	# BeautifulSoup data structure is nicer to work with
	inputTA = driver.find_element_by_id("originaltext")
	submitBtn = driver.find_element_by_id("viewhtml")

	
	# Since we cant directly set value via the driver element, need to do via javascript
	inputTA.send_keys(message)
	inputTA.send_keys(Keys.RETURN)

	submitBtn.click()

	time.sleep(1) # To let the converter do its magic

	outputTA = driver.find_element_by_id("zalgohtml")
	res = outputTA.get_attribute("value")
	# print(res)

	return res

scrapeWebsite("Test message")