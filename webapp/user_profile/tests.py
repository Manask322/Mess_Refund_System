from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
import selenium
# from selenium import page_source
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from user_registration_bs4.tests import AccountTestCase
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
# man = 0 
class ScanActionSeleniumTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(ScanActionSeleniumTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(ScanActionSeleniumTestCase, self).tearDown()
    
    #Testing Scanning
    def test_scan(self):
        selenium = self.selenium
        selenium.get('http://localhost:8000/accounts/login/')
        email = selenium.find_element_by_id('id_login')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_css_selector('button.btn.btn-primary.btn-block')
        email.send_keys('a@gmail.com')
        password.send_keys('123soham@')
        submit.click()
        selenium.get('http://localhost:8000/scan_result')
        ele = WebDriverWait(selenium,10).until(
            EC.presence_of_element_located((By.ID,"myBtn"))
        )
        selenium.quit()

    #DashBoard Testing
    def test_dashboard(self):
        selenium = self.selenium
        selenium.get('http://localhost:8000/accounts/login/')
        email = selenium.find_element_by_id('id_login')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_css_selector('button.btn.btn-primary.btn-block')
        email.send_keys('a@gmail.com')
        password.send_keys('123soham@')
        submit.click()
        print("manas" ,count)
        selenium.get('http://localhost:8000/dashboard')
        selenium.quit()
