import unittest
from selenium import webdriver

# 用类来管理测试用例
class TestCaseIndex(unittest.TestCase):
    #方法test_数字_用例名称
    def test_01_tjjc(self):
        driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        driver.get('http://81.68.125.221:8080/ljindex/')

        e = driver.find_element_by_xpath('//*[@id="articles"]/li[2]/div/div[1]')
        assert e.text == '为什么要学习测试' #python原生自带的断言
        #unittest自带的断言
        # self.assertEqual(e.text,'为什么要学习测试')
        
# 只有当前py文件运行，才会执行unittest.main()

if __name__ == "__main__":
    unittest.main()  #自动收集并收集当前文件的test方法,只是用来写脚本的时候再用它