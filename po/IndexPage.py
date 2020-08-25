from utils.seleniumtools import find_element

class IndexPage():

    def __init__(self, driver):
        self.driver = driver
        self.loginbtn = ("link text", "登录")
        
    def go_to_login_page(self):
        find_element(self.driver, self.loginbtn).click()