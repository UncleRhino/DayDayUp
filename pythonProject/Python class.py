# 类的定义
class Hero(object):
    def info (self):
        print (self)
        print ('self各不同，对象是出处')

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()
hero1.info()
hero2.info()
hero3.info()

# 对象的属性和方法
# 1、添加和获取对象的属性
class Hero (object):
    def move(self):
        print('going on')
hero=Hero()
hero.name = 'lucy'
hero.hp = 2500
print('英雄%s的生命值：%d'%(hero.name,hero.hp))
hero.move()

# 2、在方法内通过self获取对象属性
class A:
    def test(self):
        print('%s age%d'%(self.name,self.age))

a = A()
a.name='Dan'
a.age=20
a.test()



# 创建类
class B:
    num = 0
    def __init__(self,name):
        self.name = name
    def test(self):
        print(f'my name is {self.name}')

# 实例属性
b = B('zs')
print(b.name)
# 类不能访问实例属性
print(b.num)     # 对象可以访问类属性
print(B.num)     # 类也可以访问类属性
b.test()

# 1、类中封装数据
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def add(self):
        print('name is: %s,age is: %d'% (self.name,self.age))


# 创建对象s1
s1 = Student('Lucy',20)
s1.add()
# 创建对象s2
s2 = Student('Lily',25)
s2.add()

# 例：士兵设计
class Soldier:
    def __init__(self,model,name,count):
        self.model = model
        self.name = name
        self.count = count

    def shoot(self):
        if self.count <= 0:
            print ('no use')
        else:
            print (f'{self.name}used{self.model}shoot{self.count}bullet')
            self.count -=1

s = Soldier('AK47','Xu',2)
s.shoot()
s.shoot()
s.shoot()


# 私有属性
# _x 也代表是有属性或方法，实际上类对象 和子类可以访问
# __x 是有成员
# __x__用户名字空间的魔法对象或属性
# xx_ 用于避免于python关键词的冲突 class_

class Classmate:
    name = 'lucy'
    _age = 20
    __sex = 'F'

pr = Classmate()
print (Classmate.name)
print (Classmate._age)
# 强行获取私有属性 语法：对象._类名_属性名
print (pr._Classmate__sex)


# 单继承
class Person:
    Sname = 'animal'
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    def eat(self):
        print (f'{self.name}在吃东西,性别是{self.sex},年龄是{self.age}')

class Lucy(Person):
    pass
p1 = Lucy('lucy','f','18')
p1.eat()

# 继承的传递性
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print ('--吃--')
    def sleep(self):
        print ('--睡--')
class Dog(Animal):
    def bark(self):
        print (f'{self.name}汪汪叫！')

class Black(Dog):
    def fly(self):
        print(f'{self.name}说：我会飞')

black = Black('小黑')
black.fly()
black.bark()
black.eat()

# 覆盖写--重写
class Human(object):
    def __init__(self):
        self.name = zs
    def eat(self):
        print('%s在吃饭'% self.name)

class zs(Human):
    def eat(self):
        print ('%s在慢慢地吃饭'% self.name)

# 扩展父类的方法

# 1、父类名.方法（self）
class Animal(object):
    def eat(self):
        print ('吃东西')

class Dog(Animal):
    def eat(self):
        Animal.eat(self)
        print('啃骨头')

black = Dog()
black.eat()

# 2、super（）.父类方法
class Animal(object):
    def __init__(self,name):
        self.name = name
    def bark(self):
        print('%s在叫'% self.name)
        print('haha')

class Dog(Animal):
    def bark(self):
        super().bark()
        print ('%s在汪汪叫'% self.name)

white = Dog('小白')
white.bark()

# 继承父类构造方法，并进行改写
class A:
    def __init__(self,name):
        self.name = name
        print ('父类中的名字：',self.name)

    def test(self):
        print ('父类中的%s在哈哈笑'% self.name)

class A2(A):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
        print('子类中的名字：',self.name)

    def test(self):
        print ('子类中的%s在哈哈笑'% self.name)

a2 = A2('lucy')
a2.test()

# 子类对象可以通过父类的公有方法间接访问到私有属性或私有方法
class X:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print (f'私有方法{self.num1},{self.__num2}')
    def test(self):
        print('父类的公有方法d'% self.__num2)
        self.__test()


class Y(X):
    def demo(self):
        print(123)

c = Y()
print (c.num1)








