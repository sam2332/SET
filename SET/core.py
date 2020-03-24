from selenium import webdriver
import requests

from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

class Core:
    driver = None
    base_handle = None

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        if self.driver is None:
            self.startSession()
        old_page = self.driver.find_element_by_tag_name("html")
        yield
        WebDriverWait(self.driver, timeout).until(staleness_of(old_page))
        

    def __init__(self):
        pass
        
    def clickLinkByText(self,text):
        self.driver.find_element_by_link_text(text).click()
               
    def clickLinkByXPath(self,path):
        self.driver.find_element_by_xpath(path).click()
        
    def startSession(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.base_handle = self.driver.window_handles.pop()
        else:
            print('session already created, returning old')
        return self
    
    def getDriver(self):
        if self.driver is None:
            self.startSession()
        return self.driver

    def get(self, url):
        with self.wait_for_page_load():
            self.driver.get(url)

    def endSession(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
        
    def getRequestsSession(self):
        cookies = self.driver.get_cookies()
        s = requests.Session()
        for cookie in cookies:
            s.cookies.set(cookie["name"], cookie["value"])
        return s
    
    def __enter__(self):
        return self.startSession()
    
    def __exit__(self,ex_type, ex_value, ex_traceback):
        print(ex_type, ex_value, ex_traceback)
        self.endSession()
        
#https://pythonspot.com/selenium-take-screenshot/