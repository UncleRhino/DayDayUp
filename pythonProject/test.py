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