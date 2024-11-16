i = 1
while i <=10:
    print ('i love you')
    i += 1

#1-100的累计和
i = 1
sum = 0
while i <= 100:
    sum = sum +  i
    i += 1
print (f'1-100的累计和：{sum}')

#1-100偶数的累计和
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum = sum + 1
    i += 1
print ('1-100的累计偶数和:%d'% sum )

#打印小星星
i = 5
while i <= 5:
    print ('* ' * i)
    i += 1

