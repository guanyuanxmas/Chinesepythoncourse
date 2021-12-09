#global关键字
""" ex:1 """
# def demo():
#     global c
#     c = 2

# demo()
# print(c)

""" ex:2 """
c = 2
def xyz():
    global c
    c = 4
    print(c)

xyz()
print(c)
