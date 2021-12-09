#for 与 for-else循环
# #主要是用来遍历/循环 序列或者集合，字典
a = [['apple', 'orange', 'banana', 'grape'], (1,2,3)]
for x in a:
    for y in x:
        if y == 'orange':
            break  #break内部循环y不妨碍外部循环x继续
        print(y)  
else:
    print('fruit is gone')

""" 
apple
1
2
3
fruit is gone 
"""

# a = [1,2,3]
# for x in a:
#     if x == 2:
#         break
#     print(x)
# else:
#     print('eof')


# a = [1,2,3]
# for x in a:
#     if x == 2:
#         continue
#     print(x)
# else:
#     print('eof')