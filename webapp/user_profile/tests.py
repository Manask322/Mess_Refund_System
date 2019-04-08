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
class ScanActionSeleniumTestCase(AccountTestCase):

    # def setUp(self):
    #     self.selenium = webdriver.Firefox()
    #     super(ScanActionSeleniumTestCase, self).setUp()

    # def tearDown(self):
    #     self.selenium.quit()
    #     super(ScanActionSeleniumTestCase, self).tearDown()
    

    def test_scan(self):
        count = 0
        selenium = self.selenium
        #Opening the link we want to test
        print("here")
        self.test_login()
        count += 1
        # man += 1
        print("manas" ,count)
        # selenium.get('http://localhost:8000/scan_result')
        # first_name = selenium.find_element_by_id('id_first_name')
        # last_name = selenium.find_element_by_id('id_last_name')
        # try:
            # ele = WebDriverWait(selenium,10).until(
                # EC.presence_of_element_located((By.ID,"myBtn"))
            # )
        # finally:
        selenium.quit()
        return
        #check the returned result        
        
        assert "User Profile" in selenium.title        
