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