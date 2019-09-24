from selenium import webdriver


class Driver:

    def __init__(self):
        self.driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')

    def navigate(self, url):
        if isinstance(url, str):
            self.driver.get(url)
        else:
            raise TypeError("URL must be a string.")

    def current_url_value(self):
        return self.driver.current_url
        
    def close_window(self):
        self.driver.close()
