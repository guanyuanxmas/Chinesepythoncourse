#参数
#1 必须参数
#2 关键字参数


#具体事例：
def add(x,y):     #x,y是形参
    result = x + y
    return result
#c = add(y=3, x=2)   #关键字参数
a = add(1,2)   #1,2是实参
print(a)

#3 默认参数
def print_student_files(name, gender = 'female', age = 14, college = 'coc'):
    print('my name is' + name)
    print('this year' + str(age) + 'years old')
    print('i am' + gender)
    print('my school is:' + college)

print_student_files('steven','male',18,'haverd')
print("------------------------")
print_student_files('steven')

