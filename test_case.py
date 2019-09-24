import unittest
from selenium import webdriver
from page_objects import Home_Page
from web_driver import Driver




class Test_Bank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Driver()
        
    def test_home_page(self):
        home_page = Home_Page(self)
        home_page.go_to_home_page()
        

    def test_log_in(self):
        home_page = Home_Page(self)
        home_page.go_to_home_page()
        home_page.log_in()
    
        

    def test_password(self):
        home_page = Home_Page(self)
        home_page.go_to_home_page()
        home_page.log_in()
        home_page.password()
        

    def test_dropdown(self):
        home_page = Home_Page(self)
        home_page.go_to_home_page()
        home_page.log_in()
        home_page.password()
        home_page.drop_down()

    @classmethod
    def tearDownClass(cls):
        cls.driver = Driver() #webdriver.Chrome('C:\dev1\week5\chromedriver.exe')
        cls.driver.close_window()




if __name__ == '__main__':
    unittest.main()
