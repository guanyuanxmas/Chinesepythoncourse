class Student():
    teacher = 'professor bob'
    sum = 0
    
    def __init__(self,name1,age2):
        self.name = name1
        self.age = age2
        self.__class__.sum += 1  #通过self.__class__方式可以从内部调用外部类变量
        self.__score = 0
        
    def myfunc(self):  #实例方法
        print('my name is:' + self.name + ' , ' + 'my age is:' + self.age)
        
    def sing(self):
        print(self.name + ' , ' + 'is singing song now')
        
    @classmethod  #类方法
    def myfunc2(cls):
        print(cls.teacher + ' , ' + 'is good teacher')
        
    @classmethod   #类方法
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
        
    @staticmethod  #静态方法
    def add(x,y):
        print('this is a static method')
        
    def do_homework(self):
        self.do_english_homework()
        print('homework')
        
    def do_english_homework(self):
        print('english homework')
        
    def marking(self, __score):  #不想被访问在marking前加双下划线，如果前后都加双下划线默认可以访问
        if __score < 5:
            return '不能够给别人打负分'
        self.__score = __score
        print(self.name + '同学本次考试分数为:' + str(self.__score))
        
    
        
student1 = Student('aki','36')
print(student1.name + ' ' + 'is thinkin' + ',' + 'his age is:' + student1.age)
Student.plus_sum()
student1.plus_sum()
print("''''''''''''''''''''''''''''''''''''''")
student2 = Student('elisa','17')
Student.plus_sum()
print("''''''''''''''''''''''''''''''''''''''")
student2.myfunc()
print("''''''''''''''''''''''''''''''''''''''")
student1.myfunc()
print("''''''''''''''''''''''''''''''''''''''")
Student.myfunc2()
print("''''''''''''''''''''''''''''''''''''''")
student2.sing()
print("''''''''''''''''''''''''''''''''''''''")

Student.add(1, 2)
print("''''''''''''''''''''''''''''''''''''''")    #静态方法
student2.add(3, 4)

student1.do_homework()  #同时打印出了english homework和homework

result=student1.marking(2)
print(result)

student1._score = 4  #这里并不是上面实例变量self.score
print(student1._score)

print(student2._Student__score)  #通过前加一个下划线后面加两个下划线可以强制读取私有变量








        




