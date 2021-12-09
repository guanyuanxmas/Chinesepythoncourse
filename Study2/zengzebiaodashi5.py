# 匹配0次1次或者无限多次
# *匹配0次或者无限多次
# +匹配1次或者无限多次
# ?匹配0次或者1次

import re
a = 'pytho0python1pythonn2' 

r = re.findall('python*', a) # ['pytho', 'python', 'pythonn']
print(r)

r = re.findall('python+', a) # ['python', 'pythonn']
print(r)

r = re.findall('python?', a) #?前面n至少出现0次或者1次 ['pytho', 'python', 'python']
print(r)

r = re.findall('python{1,2}', a) #? n重复一次到两次 贪婪模式
print(r)

r = re.findall('python{1,2}?', a) #? n重复一次到两次 转非贪婪模式加?
print(r)
