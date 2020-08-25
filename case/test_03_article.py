import unittest
import time
from selenium import webdriver
from seleniumtools import is_logined

class TestCaseArticle(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() 
    def setUp(self):
        self.driver.get('http://81.68.125.221:8080/ljindex/')
        time.sleep(5)
        #判断用户是否登录，没有登录就去执行登录的case
        is_logined(self.driver)

    def test_01_dz(self):
        # 写点赞的case代码
        self.driver.find_element_by_xpath('//*[@id="questsions"]/li[2]/p').click()
        time.sleep(3)
        before = self.driver.find_element_by_id('question_likes').text
        self.driver.find_element_by_xpath('//*[@id="user_likes"]').click()
        time.sleep(3)
        after = self.driver.find_element_by_id('question_likes').text
        assert before != after