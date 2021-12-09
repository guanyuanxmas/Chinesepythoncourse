#变量作用域
# c = 50

# def add(x, y):
#     c = x + y
#     print(c)
# #变量的作用域
# add(1,2)
# print(c)

""" 函数内部引用外部变量，反过来是不行的 """
# c = 10 #全局变量
# def demo():
#     c = 50 #局部变量
#     print(c)

# demo()

""" 错误案例 """
# def demo():
#     c = 50  #局部变量

# print(c)
# demo()
""" 特殊情况：for 循环的外部可以引用for循环内部的变量 (这点很重要！！）"""
# def demo():
#     c = 50
#     for i in range(0, 9):
#         a = 'a'
#         c += 1   
#     print(c)
#     print(a)

#demo()

""" 函数里定义函数"""
c = 1

def func1():
    c = 2
    def func2():
        c = 3
        print(c)
    func2()
#链式，作用域链
func1()
""" 
1、变量的应用遵循就近原则
2、局部变量不能直接被外部引用，但这是相对而言的
3、作用域具有逐层引用的链式特性
 """
 




