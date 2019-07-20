from selenium import webdriver
from time import sleep
import unittest
driver = webdriver.Firefox() #Chrome
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id('su').click()
sleep(2)
title = driver.title
print(title)
driver.quit()


# #Linux 基础学习。
# ls命令
# ls -la /home 查看其他目录
# ls *txt 查看当前目录下的所有以TXT结尾的文件
#
#
#
# 读写权限：
# d  代表的是文件夹
# -  是文件
# r  代表可读
# w  代表可写
# x  代表执行
#
# 权限分为三组    前三个代表当前用户对文件的权限。
#                 中间三个，代表 这一组的用户对文件有什么权限
#         最后是，除了当前组。其他组队当前文件的权限。
#
