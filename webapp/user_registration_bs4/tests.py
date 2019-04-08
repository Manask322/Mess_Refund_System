from django.test import TestCase

# Create your tests here.
from django.test import TestCase
import selenium
# from selenium import page_source
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()
    
    def test_login(self):
        selenium = self.selenium
        #Opening the link we want to test
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

        #check the returned result        
        
        # assert "Sign In" in selenium.title    


    # def test_register(self):
    #     selenium = self.selenium
    #     #Opening the link we want to test
    #     selenium.get('http://localhost:8000/accounts/signup/')
    #     # first_name = selenium.find_element_by_id('id_first_name')
    #     # last_name = selenium.find_element_by_id('id_last_name')
    #     username = selenium.find_element_by_id('id_username')
    #     email = selenium.find_element_by_id('id_email')
    #     password1 = selenium.find_element_by_id('id_password1')
    #     password2 = selenium.find_element_by_id('id_password2')

    #     submit = selenium.find_element_by_css_selector('button.btn.btn-primary.btn-block')
    #     # (By.CSS_SELECTOR, "button.btn-primary.btn-action.bookButton#bookButton>span.btn-label"))

    #     #Fill the form with data
    #     # first_name.send_keys('Yusuf')
    #     # last_name.send_keys('Unary')
    #     username.send_keys('harsha')
    #     email.send_keys('hv2595@gmail.com')
    #     password1.send_keys('123Unary!@#')
    #     password2.send_keys('123Unary!@#')

    #     #submitting the form
    #     submit.click()

    #     #check the returned result        
        
    #     assert "Signup" in selenium.title        
