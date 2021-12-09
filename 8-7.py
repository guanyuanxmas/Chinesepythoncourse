#可变参数
#print('a','b','c')
#(), []

# def demo(*param):
#     print(param)
#     print(type(param))
# #a = (1,2,3,4,5,6)
# #demo(*a)
# """ or """
# demo(1,2,3,4,5,6)

""" 顺序：必须参数，默认参数，可变参数 """
def demo(param1, param2=2, *param):
    print(param1)
    print(param2)
    print(param)

a = (1,2,3,4,5,6)
demo(*a)
""" 返回结果 """
""" 
1
2
(3, 4, 5, 6)
 """
#if demo('a', 1,2,3)
""" 返回结果 """
""" 
a
1
(2,3)
 """
 #没有办法跳过第二个默认参数
 #another example:

def demo(param1, *param, param2=2):
    print(param1)
    print(param)
    print(param2)

demo('a', 1,2,3, param2 = 'param')
""" 返回结果 """
""" 
a
(1,2,3)
param
 """
