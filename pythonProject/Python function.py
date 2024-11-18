# 函数：把具有独立功能的代码块组合成一个个小模块
# 作用：提高代码的效率，实现代码复用————流程标准化
# 可多次调用，在不同的地方多次调用，想要使用几次就使用几次。
# 函数的定义格式
# def 函数名（）：

# import random
# help (random) #查看模块

# 如果返回多个值，是以元组形式返回
# def funa():
#   return 1,2,3
# num = funa ()
# print (num)

# 函数的参数
#def add(a,b):
#    print(a+b)
# add(3,5)

# 如果传参，则使用传参值来更新数据，有则更新，无则默认。
# def funa(a=12):
#   print (f'a={a}')
# funa(5)

# 不定长参数
# 接收多个值时，以元组的形式接收
# def funa(*args):
#    print (args)
#   print (type(args))
# funa(1,2,3)

# 参数定义顺序：必须参数（位置参数）、默认参数、可变参数、命名关键字和键字参数。
#def funa(a,b=10,*c):
#    print (f'a={a}')
#   print (f'b={b}')
#   print (f'c={c}')
# funa (1,2,3,4)

#def funa():
#    print ('-'*10)
# def funb(num):
#    i = 0
#   while i < num:
#       funa()
#       i += 1
#funb(4)

# 不同的函数可以定义相同的局部变量
# def funa():
#    a = 1
#   print ('funa第一次的值：%s' % a)
#   a = 2
#   print ('funa第二次的值：%s' % a)
# def funb():
#   a = 3
#    print ('funb第一次的值：%s' % a)

# 全局变量
li=[]
for i in range (5):
    li.append (i)
    print (li)
print (li)

a = 100
def funa():
    print (a)
def funb():
    print (a)
funa()
funb()

# 匿名函数：对简单函数的定义
# 语法：函数名 = lambda 形参：返回值。形参的数量按需加，加多少都可以，只要用逗号隔开即可。
# lambda是定义匿名函数的关键字，相当于函数的def
# 调用：结果 = 函数名（实参）
def func(a,b):
    return a+b
print (func(1,2))

func = lambda a,b:a+b
print (func(1,2))

# 求平方
a = lambda x:x**2
print (a(10))

import builtins
print (dir(builtins))

a = [1,2,3]
b = ['a','b','c']
print (list(zip(a,b)))

# enumerate枚举：用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中。
li = ['a','b','c','d']
for i ,j in enumerate(li):
    print(i,j)

