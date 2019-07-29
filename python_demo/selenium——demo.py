import unittest
from time import sleep
from selenium import webdriver

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")

    def testSearch(self):
        driver = self.driver
        driver.find_element_by_id('kw').send_keys("selenium")
        sleep(2)
        expectvalue = "selenium_百度搜索"
        realvalue = driver.title
        self.assertEqual(expectvalue,realvalue)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()