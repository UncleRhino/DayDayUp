# 标准装饰器的模版
#def wrapper (func):
#   def inner (*args,**kwargs):
#       ret = func(*args,**kwargs)
#       return ret
#   return inner

# 日志打印器
def logger(func):
    def wrapper(*args):
        print ('我准备开始计算：{}函数了：'.format(func.__name__))
        func(*args)
        print ('我计算完了')
    return wrapper
def add(x,y):
    print ('{}+{}={}'.format(x,y,x+y))
te = logger (add)
te(200,50)

# 无参数的函数（被装饰的函数（业务函数）无参数
# 装饰器函数本质：通过业务作为参数传入到装饰器函数里面

#装饰函数
def test (fn):
    def inner():
        print('this is inner')
        fn()
    return inner
# 方法一 def t1():
#    print('hhhh')
# t=test(t1)
# t()
# 方法二
@test
def t1():
    print('hahaha')
t1()

# 二 被装饰的函数有参数
def exam (fn):
    def inner(a,b):
        fn(a,b)
    return inner
@exam
def test(a,b):
    print ('turn out:',(a+b))
test(1,2)

# 多层嵌套
def exam(fn):
    def funa(x,y):
        print ('hello',x,y)
        def inner(a,b):
            print ('inner函数的值：%s,%s'%(a,b))
            fn(a,b)
        return inner
    return funa

@exam
def test (a,b):
    print ('turn out:',(a+b))
test(1,2)(3,4)

# 被装饰的函数有不定长参数
# 函数参数定义顺序：必选参数、默认参数、可变参数、命名关键字和关键字参数
def funa(fn):
    def inner(*args,**kwargs):
        print('start: {}',fn.__name__)
        fn(*args,**kwargs)
        print('end')
    return inner

@funa
def add(*a,**b):
    print(a)
    print(b)

add(2,3,4,5,6,a=1,b=3)






