from utils.seleniumtools import find_element

class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
        # 封装要用到的元素
        self.username = ("id", "username")
        self.password = ("id", "password")
        self.loginbtn = ("id", "userLogin")
        self.forgetps = ("link text", "忘记密码？")
        self.userregs = ("link text", "注册")

    def login(self, u, p):
        """
            登录
        """
        find_element(self.driver, self.username).send_keys(u)
        find_element(self.driver, self.password).send_keys(p)
        find_element(self.driver, self.loginbtn).click()
        
    def go_to_forget_password(self):
        find_element(self.driver, self.forgetps).click()

    def go_to_reg(self):
        find_element(self.driver, self.userregs).click()