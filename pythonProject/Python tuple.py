# 元组的特征：不能被修改,不支持删除。
# 元组的定义：元素由小括号包围，每个元素之间用逗号隔开。如（1，2，3）
# 意义：因为元组不能修改和删除，所以提高了代码编写的安全性。
num_list = (10,20,30)
print (num_list[0])

# 定义多个数据元组
t1 = (10,20,30)
print (t1)
# 定义单个元组的时候必须要加逗号
t2 = (10)
print(t2)
t3 = (10,)
print (t3)

print (type(t3))

# 字典的运用场景
# 存储多哥数据
# 字典的特性：键值对成对出现，键和值一一映射，绑定的关系
# 字典数据和数据顺序没有关系，即字典不支持下标，后期无论数据如何变化，只需要按照对应的键来查找数据即可。
# 定义：符号是打括号，数据为“键值对”形式出现，各个键值对之间用逗号隔开。
# 键值对是一一对应的关系，可理解为绑定对应，key：vale
# key是唯一的
# 方法一：dict1 = {'name':'Tom,'age':20,'gender':'男'}
# 定义空字典：
# 方法一：dict2 = {}
# 方法二：dict3 = dict（）

# 集合的定义：大括号包围元素，每个元素用逗号隔开。
# 与字典的区别：字典键值对一一对应关系，集合没有。
s1 = {10,20,30}
print (type(s1))
print (s1)

# 定义：用set（）
s2 = set ('abcdef')
print (type(s2))
print (s2)
# 定义一个空集合
s3 = set ()
print (type(s3))
print (s3)

# 列表推导式
list = [i for i in range (10)]
print (list)

# 元组推导式
t1 = (i for i in range (10))
print (t1) # 返回的地址
print (tuple(t1))

# 字典推导式
dict1 = {i:i**2 for i in range(1,5)}
print (dict1)

#集合推导式
list1 = [1,1,2]
set1 = {i**2 for i in list }
print (set1)


# 类型转换的特性：你想要获取什么的类型，就用什么样的函数即可。
a = 5
print (type(a))
b = str(a)
print (b,type(b))

# dict（）转换在字典
a = ['a1','a2','a3','a4']
b = ['b1','b2','b3']
d = zip (a,b)
print (d)
print (dict(d))

# 定义列表
a = [1,2,3,4]
print (a,id(a))
b = a
print (b,id(b))

# 拷贝
import copy
a = [1,2,3,4,5]
a_copy =copy .copy(a)
print (a_copy)







