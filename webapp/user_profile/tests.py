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
    

    # def test_scan(self):
    #     count = 0
    #     selenium = self.selenium
    #     #Opening the link we want to test
    #     print("here")
    #     print("I am here")
    #     selenium.get('http://localhost:8000/accounts/login/')
    #     # first_name = selenium.find_element_by_id('id_first_name')
    #     # last_name = selenium.find_element_by_id('id_last_name')
    #     email = selenium.find_element_by_id('id_login')
    #     # email = selenium.find_element_by_id('id_email')
    #     password = selenium.find_element_by_id('id_password')
    #     # password2 = selenium.find_element_by_id('id_password2')

    #     submit = selenium.find_element_by_css_selector('button.btn.btn-primary.btn-block')
    #     # (By.CSS_SELECTOR, "button.btn-primary.btn-action.bookButton#bookButton>span.btn-label"))

    #     #Fill the form with data
    #     # first_name.send_keys('Yusuf')
    #     # last_name.send_keys('Unary')
    #     # userna.send_keys('harsha')
    #     email.send_keys('a@gmail.com')
    #     password.send_keys('123soham@')
    #     # password2.send_keys('123Unary!@#')

    #     #submitting the form
    #     submit.click()
    #     count += 1
    #     # man += 1
    #     print("manas" ,count)
    #     selenium.get('http://localhost:8000/scan_result')
    #     # first_name = selenium.find_element_by_id('id_first_name')
    #     # last_name = selenium.find_element_by_id('id_last_name')
        
    #     ele = WebDriverWait(selenium,10).until(
    #         EC.presence_of_element_located((By.ID,"myBtn"))
    #     )
    #     selenium.quit()
        # return
        #check the returned result        
        
        # assert "User Profile" in selenium.title      

    def test_dashboard(self):
        count = 0
        selenium = self.selenium
        #Opening the link we want to test
        print("here")
        print("I am here")
        selenium.get('http://localhost:8000/accounts/login/')
        # first_name = selenium.find_element_by_id('id_first_name')
        # last_name = selenium.find_element_by_id('id_last_name')
        email = selenium.find_element_by_id('id_login')
        # email = selenium.find_element_by_id('id_email')
        password = selenium.find_element_by_id('id_password')
        # password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_css_selector('button.btn.btn-primary.btn-block')
        # (By.CSS_SELECTOR, "button.btn-primary.btn-action.bookButton#bookButton>span.btn-label"))

        #Fill the form with data
        # first_name.send_keys('Yusuf')
        # last_name.send_keys('Unary')
        # userna.send_keys('harsha')
        email.send_keys('a@gmail.com')
        password.send_keys('123soham@')
        # password2.send_keys('123Unary!@#')

        #submitting the form
        submit.click()
        count += 1
        # man += 1
        print("manas" ,count)
        selenium.get('http://localhost:8000/dashboard')
        # first_name = selenium.find_element_by_id('id_first_name')
        # last_name = selenium.find_element_by_id('id_last_name')
        
        # ele = WebDriverWait(selenium,10).until(
        #     EC.presence_of_element_located((By.ID,"myBtn"))
        # )
        selenium.quit()
