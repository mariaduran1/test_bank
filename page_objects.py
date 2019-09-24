from selenium import webdriver
from web_driver import Driver
from selenium.webdriver.common.keys import Keys
import strings

class Home_Page:

    def __init__(self,driver):
        self.driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')

    def go_to_home_page(self):
        self.driver.get(strings.url)
        self.driver.save_screenshot("pic.png")
    
    def log_in(self):
        user_id = self.driver.find_element_by_id("login-user")
        user_id.send_keys(strings.user_name)
        self.driver.save_screenshot("pic2.png")

    def password(self):
        password_el = self.driver.find_element_by_id("login-password")
        password_el.send_keys(strings.password)
        self.driver.save_screenshot("pic3.png")
        

    def drop_down(self):
        drop_d = self.driver.find_element_by_id("manage")
        drop_d.click()
        card = self.driver.find_element_by_xpath('//*[@id="manage"]/option[2]')
        card.click()
        self.driver.save_screenshot("pic4.png")
        


