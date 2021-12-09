import re

a = 'C0C++7Java8C#9Python6Javascript'   #提取字符串例所有的数字0-9

#r = re.findall('\d', a)
#print(r)

r = re.findall('\D', a)
print(r)

#'Python' 普通字符 , '\d' 是元字符，等价于[0-9]  '\D' 是非数字

