from selenium import webdriver
import requests

class Core():
	driver = None
	base_handle = None

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
