#关键字可变参数(1)
def squsum(*param):
    sum = 0
    for i in param:
        sum += i*i
    print(sum)

squsum(1,2,3,4,5,6)
""" or """
#squsum(*[1,2,3,4,5,6])

#关键字可变参数(2)
def city_temp(**param):
    for key, value in param.items():
        print(key, value)
    
city_temp(bj='32c', xm='23c', sh='31c')
""" or """
# a = {'bj:'32','xm':'23','sh':'31c'}
#city_temp(**a)


