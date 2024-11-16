#计算1-100求和
sum = 0
for i in range(1,101):
    sum = sum + i
print (f'求和结果为{sum}')

#九九乘法表
for row in range(1,10):
   for col in range(1,row+1):
        print (f'{col}  * {row} = {col * row}',end='\t')
print ()

#break
a = 0
while a < 5:
    a = a+1
    if a==3:
        break
    print (a)
else:
    print ('打印已完成')

# break只对当前所在循环有效
# 循环嵌套中的break
for i in range (5):
    print ('haha')
    for i in range (3):
        if i == 2:
            break
        else:
            print (i)

# continue 结束循环，结束当前循环的，continue后面的代码不再执行，继续下一轮
a = 0
while a < 5:
    a = a + 1
    if a == 3:
        continue
    print (a)

#find语法
a = 'hello world'
print (a.find('h'))
print (a.find('hello'))
print (a.find('1',1,5))


#find语法
a = 'hello world'
print (a.find('h'))
print (a.find('hello'))
print (a.find('1',1,5))
