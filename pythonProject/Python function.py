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


# 递归函数的特性：
# 1）必须又一个明确的结束条件
# 2）每次进入更深一层递归时，问题规模相比上次递归都应有所减少
# 3）相邻两次重复之前有紧密的联系，前一次要为后一次做准备
# 4）递归效率不高，递归层次过多会导致栈溢出
# 5）优点：定义简单，逻辑清晰

# 递推：给递归实现拆解，递归每一次都是基于上一次进行下一次的执行
# 回溯：遇到终止条件之前，从最后往回返，一级一级的把值返回来

def funa(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print (sum)
funa(3)

# 用递归函数求斐波那契函数序列
# def funa (n):
#   if n <=1:
#        return n
#    else:
#       return funa (n-1)+funa (n-2)
# for i in range(1,11):
#    list.append(funa(i))
# print(list)

# 闭包函数
def outer(a):
    n = 10
    def inner():
        n = 20
        print ('inner',n+m)
    return inner

# 修改外部函数中的变量
def outer (a):
    def inner():
        nonlocal a
        a += 1
        print(a)
    return inner
ot = outer(1)
ot()

#回调函数
def test(m,n):
    if m ==2:
        n()
    else:
        print('No')
def one():
    print('function1')

def two():
    print('function2')

test(2,one)

# 创建对象的时候就已经拥有属性
# init 具有初始化作用，当该类被实例化时就自动执行该函数。那么把初始化的属性放在这个方法里去。
class Hero:
    def __init__(self):
        self.name = 'lulu'
        self.hp = 200
        self.at = 450
    def move(self):
        print(f'{self.name} moving on')
    def attack(self):
        print(f'{self.name} life {self.hp},then {self.at}')
hero = Hero()
hero.move
hero.attack()

# __del__析构函数

class Person:
    def __init__(self):
        print('我是init方法')
    def __del__(self):
        print('被销毁')
xm = Person()
print('last one')
print('last one')
print('last one')
def funa():
    print(123)
funa()
# 手动删除对象

class Person:
    def __init__(self):
        print('我是init方法')
    def __del__(self):
        print('被销毁')

xm = Person()
del xm
print('last one')
