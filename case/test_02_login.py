import unittest, time
from selenium import webdriver
from po.IndexPage import IndexPage
from po.LoginPage import LoginPage


@unittest.skip("跳过测试用例执行")
class TestCaseLogin(unittest.TestCase):

    def test_01_login_success(self):
        # 就是selenium的内容
        driver = webdriver.Chrome(executable_path="driver/chromedriver")
        driver.get("http://81.68.125.221:8080/ljindex/")
        time.sleep(5)
        driver.find_element_by_link_text('登录').click()
        time.sleep(5)
        driver.find_element_by_id("username1").send_keys("liuyun1")
        driver.find_element_by_id("password").send_keys("a12345678")
        driver.find_element_by_id("userLogin").click()

        time.sleep(10)
        assert driver.title == "测谈网"
        
    def test_02_po_login(self):

        driver = webdriver.Chrome(executable_path="driver/chromedriver")
        driver.get("http://81.68.125.221:8080/ljindex/")
        time.sleep(5)
        index_page = IndexPage(self.driver)
        index_page.go_to_login_page()
        
        time.sleep(5)

        # 实例化page类，直接调用方法就可以登录了
        login_page = LoginPage(self.driver)
        login_page.login("liuyun1", "a12345678")




# 只有在当前py文件运行，才会执行unittest.main()
if __name__ == "__main__":
    unittest.main()  # 自动收集并收集当前文件的test方法，只是用来写脚本的时候再用它