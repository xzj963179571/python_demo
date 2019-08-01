# _*_ coding:UTF-8 _*_

import unittest
class UserTestCase(unittest.TestCase):
    """setup()用于测试前的初始化工作；"""
    def setUp(self):
        print("===setup==")
        self.name = "小D课堂"
    """tearDown（）测试后的清除工作，在每个测试方法运行时被调用"""
    def tearDown(self):
        print("===tesrDown===")

    def test_name(self):
        print("===test_name===")
        self.assertEqual(self.name,"小D课堂",msg="名字不对")  #断言字符串是否一致
        self.assertTrue('xdclass'.isupper(),msg="不是大写")  #断言字符串是否为大写

"""注意
1.所有类中方法的入参为self，定义方法的变量也要self.变量
2.定义测试用例，以test开头命名的方法，方法的入参为self
3.unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行他们
4.自己写的py文件不能，用unittest.py命名，不然会找不到testcase
成功是输入.失败是F
"""


if __name__ == '__main__':
    unittest.main()