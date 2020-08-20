import unittest
import time
from selenium import webdriver

class TestCaseLogin(unittest.TestCase):
    def test_01_login_success(self):
        driver = webdriver.Chrome(executable_path='driver\\chromedriver.exe')
        driver.get('http://81.68.125.221:8080/ljindex/')
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_link_text('登录').click()
        time.sleep(5)
        driver.find_element_by_id('username').send_keys('liuyun1')
        driver.find_element_by_id('password').send_keys('a12345678')
        driver.find_element_by_id('userLogin').click()
        time.sleep(5)
        assert driver.find_element_by_link_text('测谈网').text == '测谈网'
        print("登录成功")
if __name__ == "__main__":
    unittest.main()  #自动收集并收集当前文件的test方法,只是用来写脚本的时候再用它