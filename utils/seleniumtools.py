from selenium.webdriver.support.ui import WebDriverWait
import time
def find_element(driver, locator, timeout=30):
    """
        方法名：动态查找元素:显式等待
        参数：
            driver: 浏览器的句柄/把柄
            locator: 元素定位方式
                格式： 
                    - ("id", "username")
                    - ("name", "username")
                    - ("class name", "username")
                    - ("xpath", "username")
                    - ("css selector", "username")
                    - ("link text", "username")
                    - ("partial link text", "username")
            timeout: 超时间时间，默认10
        返回值：
            - 找到元素：返回元素
            - 没找到元素：直接报错:timeout
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))

def is_logined(driver):
    """
        判断用户是否登录
    """
    try:
        driver.find_element_by_link_text('登录').click()
        #用户未登录，去执行用户登录的代码
        time.sleep(3)
        driver.find_element_by_id('username').send_keys('liuyun1')
        time.sleep(1)
        driver.find_element_by_id('password').send_keys('a12345678')
        time.sleep(1)
        driver.find_element_by_id('userLogin').click()
    except Exception as e:
        print(e)
        # 没有找到登录按钮，已经登录了