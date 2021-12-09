def my_avg(a,b):
    return (a+b)/2

#如下是函数的调用
c = my_avg(20,30)
print(c)

""" 如何让函数返回多个结果 """
def damage(skill1, skill2, skill3):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    damage3 = skill3 * 4
    return damage1, damage2, damage3

skill1_damage, skill2_damage, skill3_damage = damage(3,6,7)
""" 序列解包 """
print(skill1_damage, skill2_damage, skill3_damage) 
"""下面索引方式并不好"""
#damages = damage(3,6,7)
#print(damages[0], damages[1], damages[2])
"""序列解包说明  """
a = 1
b = 2
c = 3

a,b,c = 1,2,3

d = 1,2,3  #d是一个tuple
print(type(d))
a,b,c = d
""" 更简单的方法 """
a = 1
b = 1
c = 1
a=b=c=1
print(a,b,c)
