#概括字符集 
# \d \D
# \w 只能匹配单词字符 等同于 [A-Za-z0-9_]  *最后下划线也可以匹配到
# \W 匹配非单词字符&,空格，|\n,\t| 也属于非单词字符
# \s 空白字符
# \S 匹配非空白字符

# 数量词

import re
#a = 'python 11\t11java&__678p\nh\rp'

#r = re.findall('[0-9]', a)   #0-9 and \d result same 
#print(r)

#r = re.findall('\w', a)   #匹配字母，数字，下划线
#print(r)

#r = re.findall('\s', a)   #匹配到了非单词字符&
#print(r)

a = 'python 1111java678php' #单词数量最小的是3最大的事6，所以下面大括号写3，6

r = re.findall('[a-z]{3,6}?', a)  # ['pyt', 'hon', 'jav', 'php']->[a-z]{3}  #['python', 'java', 'php']->[a-z]{3,6}
#贪婪 与 非贪婪  Python默认是贪婪的模式匹配  非贪婪的模式在6后面加? 结果和只加3结果一样['pyt', 'hon', 'jav', 'php']
print(r)