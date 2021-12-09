#for与range
# """ 0-10 递增"""
# for x in range(0,10,2):   #第二个数字在range里表示偏移量,第三个数字表示步长
#     print(x, end = '|')
# """ 0|2|4|6|8 """

# """ 0-10 递减"""
# for x in range(10,0,-2):   #第二个数字在range里表示偏移量,第三个数字表示步长
#     print(x, end = '|')
# """ 10|8|6|4|2 """


a = [1,2,3,4,5,6,7,8]
""" method 1 """
# for i in range(1,len(a),2):
#     print(i)
""" method 2 """
b = a[0:len(a):2]
print(b)

