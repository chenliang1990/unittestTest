import unittest, time
from selenium import webdriver
from utils.seleniumtools import is_logined

class TestCaseAdminIndex(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://qk.mrhkj.com/admin/common/login.html")
        self.driver.delete_all_cookies()
        cookie = {'domain': 'qk.mrhkj.com', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'ub1h1c7gqj6itoen63v69ssrfh'}
        self.driver.add_cookie(cookie)
        self.driver.refresh()
        time.sleep(5)

    def test_01_user_count(self):
        e = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div/span[2]")
        assert e.text == 101

    def test_02_file_count(self):
        e = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/div/div/span[2]")
        assert e.text == 2