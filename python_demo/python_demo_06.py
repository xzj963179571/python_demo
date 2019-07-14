#coding=utf-8
#python中的面对对象，类，方法，对象。
#Python中的self
# class Ball:
#     def setName(self,name):
#         self.name = name
#
#     def kick(self):
#         print("我叫%s, 该死的，谁踢我" % self.name)

#
# a = Ball()
# a.setName("A")
# b = Ball()
# b.setName("B")
# c = Ball()
# c.setName("C")
# a.kick()
# b.kick()
# c.kick()


# # __init__(self)   构造方法
# class Ball:
#     def __init__(self,name):
#         self.name = name
#     def kick(self):
#         print("我叫%s, 该死的，谁踢我" % self.name)
# #
# b = Ball("B")
# b.kick()




# #公有私有
# p = Person()
# p.name
# class Person:
#     name = "小甲鱼"
#
# p = Person()
# print(p.name)
#
# class Person:
#     __name = "小甲鱼"
#
#     def getname(self):
#         return self.__name
#
#
#
# p = Person()
# print(p.getname())



# 子类，父类，超类，基类
# 如果子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性
# class Parent:
#     def hello(self):
#         print("正在调用父类的方法")
#
# class Child(Parent):
#     def hello(self):
#         print("正在调用子类的方法。。")
# #
# p = Parent()
# print(p.hello())
#
# c = Child()
# print(c.hello())
#


#
# # 实例作业
# import random as  r
# class fish:
#     def __init__(self):
#         self.x = r.randint(0,10)
#         self.y = r.randint(0,10)
#
#     def move(self):
#         self.x -= 1
#         print("我的位置是：",self.x,self.y)
# class Goldfish(fish):
#     pass
#
# class Carp(fish):
#     pass
# class Salmon(fish):
#     pass
#
# class shark(fish):
#     def __init__(self):
#         super.__init__()
#         # fish.__init__(shark)  两种方法
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print("吃货的梦想就是天天有的吃")
#             self.hungry = False
#         else:
#             print("太撑了，吃不下了")
#
# fish = fish()
# print(fish.move())
# print(fish.move())
# goldfish = Goldfish()
# print(goldfish.move())
# print(goldfish.move())
# shark = shark()
# print(shark.eat())
# print(shark.eat())
# print(shark.move())




# 多重继承

# class Base1:
#     def foo1(self):
#         print("我是foo1，我为base1代言")
#
# class Base2:
#     def foo2(self):
#         print("我是foo2，我为base2代言")
#
# class C(Base1,Base2):
#     pass
# c = C()
# print(c.foo1())
# print(c.foo2())




# 组合
# class Turtle:
#     def __init__(self,x):
#         self.num = x
# class Fish:
#     def __init__(self,x):
#         self.num = x
# class Pool:
#     def __init__(self,x,y):
#         self.turtle = Turtle(x)
#         self.fish = Fish(y)
#
#     def print_num(self):
#         print("水池里总共有乌龟 %d 只，小鱼 %d 条。" % (self.turtle.num,self.fish.num))
#
# pool = Pool(1,10)
# print(pool.print_num())


# 类 类对象，
"""
类定义             C
类对象             C
实例对象    a       b       c
不要试图在一个类里面定力出所有能想到的特性各方法，应该利用继承和组合机制来进行扩展。
用不同的词性命名，如属性名用名词，方法名用动词。


"""

# class C:
#     count = 0



# 什么事绑定
"""
Python 严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓的绑定概念"""



# 一些类。对象相关的BIF
# isinstance()检查是否属于一个类
# issubclass()检查时候是一个子类
# hasattr()检测是否存在
# getattr()
# setattr()
# property属性设置属性
