import keyword

s='HelloWord'
# 切片操作
s1=s[0:5:2]
print(s1)
# 省略了开始位置，start默认从0开始
print(s[:5:1])
# 省略开始位置start，省略不步长step
print(s[:5:])
print("hello word")

a=10
print(a)

b=5
print(b)


print ("hello\nhello")

a= "hello"
b= "word"
print ((a + "***" +b + "\n") *2)

a= "hello"
b= "word"
print ('{} {}'.format(a,b))


# 转化成整型 int（）
st = '123'
print (type (st))
st2 = int (st)
print (type(st2))

# 转换为浮点型 float（）
a = 123
b = float (a)
print (b)
print (type(b))

# input ()输入函数
input('请输入：')
print(23)

# if嵌套 练习 公交车上车判断
money = True
sit = True
if money:
    print('请上车')
    if sit:
        print('你可以坐在座位上')
    else:
        print('请站着')
else:
    print('没有钱不能上车')


# import random模块
import random
ni = int(input('请出拳：剪刀（0），石头（1），布（2）：'))
com = random.randint (0,2)
print (f'电脑的出拳{com}')

if ((ni == 0) and (com == 2)) or ((ni == 1) and (com == 0)) or ((ni == 2) and (com ==1)):
    print ('恭喜你，手气不错，赢了')
elif ni == com:
    print ('平局，要不再来一局')
else:
    print ('很遗憾你输了，洗洗手再来')


