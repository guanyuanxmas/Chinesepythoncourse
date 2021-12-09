import re
s = 'abc, acc, adc, aec, afc, ahc'       #字符集

#r = re.findall('a[cf]c', s)    #找出中间的字母是c或f的单词
#print(r)

#r = re.findall('a[cfd]c', s)   #找出中间的字母是c或f或d的单词
#print(r)

#r = re.findall('a[^cfd]c', s)   #找出中间的字母不是c或f或d的单词
#print(r)

r = re.findall('a[c-f]c', s)   #找出中间的字母c-f的单词
print(r)
