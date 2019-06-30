#coding:utf-8
# 第三次任务

# 打印水仙花数
"""
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

条件：它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
"""

for i in range(100,1000):
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == i:
        print(i,end=",") # 打印结果：153,370,371,407,

# 完美数

for a in range(1,1000):
    sum = 0
    for o in range(1,a):
        if a % o == 0:
            sum += o
    if sum == a:
        print(a)



#输出Fibonacci数列

a = 0
b = 1
while b<100:
    print(b)
    a = b
    b = a+b





# 笔记
"""
while 循环	在给定的判断条件为 true 时执行循环体，否则退出循环体。
for 循环	重复执行语句
嵌套循环	你可以在while循环体中嵌套for循环

break 语句	在语句块执行过程中终止循环，并且跳出整个循环
continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
pass 语句	pass是空语句，是为了保持程序结构的完整性。



"""

