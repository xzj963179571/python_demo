# coding = UTF-8
# 字符串的使用 |字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。

# var1 = 'Hello World!'
# var2 = "Alex"

# Python 访问子字符串，可以使用方括号来截取字符串

# print ("var1[0]: ", var1[0])
# print ("var2[1:4]: ", var2[1:4])

# Python 字符串更新
# var1 = 'Hello World!'
# print ("已更新字符串 : ", var1[:6] + 'Runoob!')



# 列表
# 序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
#
# list1=[] #创建一个空列表
# list2=[1,2,3,4]
# list3= ["b","b","c","d"]
# # 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
# print("list2[0]:",list2[0])
# print("list2[1:5]:",list2[1:5])


# 你可以对列表的数据项进行修改或更新
# list = ['Google', 'Runoob', 1997, 2000]
# print("第三个元素为：",list[2])
# list[2]=2001  #修改列表中的单个元素
# print("更改后的第三个元素为：",list[2])

# 可以使用 del 语句来删除列表的的元素
# list = ['Google', 'Runoob', 1997, 2000]
# print("原始列表：",list)
# del list[2]
# print("删除第三个元素：",list)

# 切片
# # Python中符合序列的有序序列都支持切片（slice），例如列表，字符串，元组
# 格式：【start: end:step】
#
# start: 起始索引，从0开始，-1
# 表示结束
#
# end：结束索引
#
# step：步长，end - start，步长为正时，从左向右取值。步长为负时，反向取值
#
list = ['Google', 'Runoob', 1997, 2000]
print(list[:3])
print(list[3:])
print(list[::3])
print(list[::-1])
print(list[4:2:-2])

# 实例

s = 'abcdefg'
# 返回从起始位置到索引位置 2 处的字符串切片
print(s[:3]) # 输出 'abc'

# 返回从第三个索引位置到结尾的字符串切片
print(s[3:]) # 输出 'defg'
# 字符串逆序输出

print(s[::-1]) # 输出 'gfedcba'

# 输出从开始位置间隔一个字符组成的字符串
print(s[::2]) # 输出 'aceg'
print(range(10)[::2])  # 输出偶数：[0, 2, 4, 6, 8]

# 它们也可以相互结合使用。
# 从索引位置 6 到索引位置 2，逆向间隔一个字符
print(s[6:2:-2]) # 输出'ge'

