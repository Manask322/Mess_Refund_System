from django.test import TestCase

# Create your tests here.
from django.test import TestCase
import selenium
# from selenium import page_source
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


class AccountTestCase():

    # def setUp(self):
    #     self.selenium = webdriver.Firefox()
    #     super(AccountTestCase, self).setUp()

    # def tearDown(self):
    #     self.selenium.quit()
    #     super(AccountTestCase, self).tearDown()
    
    
    #Testing Login
    def test_login(self,selenium):
        selenium = self.selenium
        print("I am here")
        selenium.get('http://localhost:8000/accounts/login/')
        email = selenium.find_element_by_id('id_login')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_css_selector('button.btn.btn-primary.btn-block')
        email.send_keys('a@gmail.com')
        password.send_keys('123soham@')
        submit.click()

    #Testing Registration
    def test_register(self):
        selenium = self.selenium
        selenium.get('http://localhost:8000/accounts/signup/')
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_css_selector('button.btn.btn-primary.btn-block')
        username.send_keys('harsha')
        email.send_keys('hv2595@gmail.com')
        password1.send_keys('123Unary!@#')
        password2.send_keys('123Unary!@#')
        submit.click()   
        assert "Signup" in selenium.title        
