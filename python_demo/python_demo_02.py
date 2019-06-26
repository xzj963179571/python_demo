#  输入温度
a = float(input("请输入摄氏温度： "))
b = float(input("请输入华氏温度： "))

# 转换温度
c = a*9/5+32
d = 5/9*(b-32)

# 输出结果
print("摄氏温度{}转换为华氏温度为：{}".format(a,c))
print("华氏温度{}转换为摄氏温度为：{}".format(b,d))



# 计算圆的面积
r = int(input("请输入圆的半径： "))
pi = 3.142
s = pi * (r*r)

print("圆的面积为：",s)



# 判断是否是闰年

year = int(input("请输入年份:"))

if ((year % 4 ==0) and year % 100 !=0) or (year % 400 == 0):
    print("是闰年")
else:
    print("不是闰年")



# input 函数
# str = input("请输入:")
# print("你输入的内容是： ",str)
# --------------------
# open函数--写
"""
f = open("D:/test_demo/python.txt","w")
f.write("python 是一个非常好的语言。 \n是的,的确非常好！！\n")
f.close()"""
# f = open("D:/test_demo/python.txt","r")
"""---读
str =f.read()
print(str)
f.close()

"""


#---读一行
# str = f.readline()
# print(str)



# str = f.readlines()
# print(str)

#
# for line in f:
#     print(line,end='')
#
# f.close()
























