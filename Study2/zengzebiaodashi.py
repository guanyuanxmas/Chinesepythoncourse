import re

a = 'C|C++|Java|C#|Python|Javascript'

r = re.findall('Python', a)
if len(r) > 0:
    print('字符串中包含Python')
#print(r)    #返回的python是个列表

r = re.findall('PHP', a)
if len(r) > 0:
    print('字符串中包含Python')   #什么都不会打印



#print(a.index('Python')> -1) #这样的内置函数可以用来判定是否以上字符串列包含Python

#print('Python' in a )

