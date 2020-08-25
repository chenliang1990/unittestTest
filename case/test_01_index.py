import unittest
import time
from selenium import webdriver

# 用类来管理测试用例
class TestCaseIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() 
    def setUp(self):
        self.driver.get('http://81.68.125.221:8080/ljindex/')
        time.sleep(3)
    def tearDown(self):
        print("这是teardown")
    #方法test_数字_用例名称  推荐教程
    def test_01_tjjc(self):        
        e = self.driver.find_element_by_xpath('//*[@id="articles"]/li[2]/div/div[1]')
        assert e.text == '为什么要学习测试' #python原生自带的断言
        #unittest自带的断言
        # self.assertEqual(e.text,'为什么要学习测试')
        # self.assertNotEqual(1,2)
        # assert 1!= 2
    def test_02_question(self):
        e = self.driver.find_element_by_xpath('//*[@id="questsions"]/li[2]/p')
        assert e.text == "why to clean?"
# 只有当前py文件运行，才会执行unittest.main()

if __name__ == "__main__":
    unittest.main()  #自动收集并收集当前文件的test方法,只是用来写脚本的时候再用它