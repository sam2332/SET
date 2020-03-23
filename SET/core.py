from selenium import webdriver
import requests

from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import  staleness_of
class Core():
	driver = None
	base_handle = None

	@contextmanager
	def wait_for_page_load(self, timeout=30):
		old_page = self.driver.find_element_by_tag_name('html')
		yield
		WebDriverWait(self.driver, timeout).until(
			staleness_of(old_page)
		)


	def __init__(self):
		pass
	
	def startSession(self):
		self.driver = webdriver.Chrome()
		self.base_handle = self.driver.window_handles.pop()
	
	def getDriver(self):
		return self.driver

	def endSession(self):
		self.driver.quit()

	def getRequestsSession(self):
		cookies = self.driver.get_cookies()	

		s = requests.Session()
		for cookie in cookies:
			s.cookies.set(cookie['name'], cookie['value'])
		return s
