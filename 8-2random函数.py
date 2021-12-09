#函数的定义及运行特点
#定义函数的方法：def
# def funcname(parameter_list):
#     pass

#parameter_list（参数列表）可以没有

#可以使用return来返回函数的结果（value），若没有return，函数结果会被认为是None

#具体事例：
# def add(x,y):     #x,y是形参
#     result = x + y
#     return result
# a = add(1,2)   #1,2是实参
# print(a)

# def add(x,y):
#     result = x + y
#     print(result)
# add(1,2)


#只有在和函数被定义后才可以使用

#错误事例：

#设置最大递归次数：sys
""" 
import sys
sys.setrecursionlimit(1000000) 
"""
""" 
def print(code):
    print(code) 
print('python')
"""
#定义的函数名与内部使用的函数重复，循环调用，无解
def print_code(code):
    print(code)
b = print_code('pythonn')
print(b)
""" 
pythonn
None 
"""

def coc(x):
    a = round(x, 2)
    return a
q = coc(1.2342)
print(q)

import random
def coc(x):
    a = random.randrange(1, x)
    return a
q = coc(10)
print(q)

import random

print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,10,2) )   # 生成从1到100的间隔为2的随机整数

a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(a)