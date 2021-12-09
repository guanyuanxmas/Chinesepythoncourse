from demo2 import Human

class Student(Human):      #Student是子类，Human是父类    父类在demo2

    def __init__(self, school, name, age):
        self.school = school 
#      Human.__init__(self, name, age)   #子类方法调用父类方法，这种方式并不推荐
        super(Student, self).__init__(name, age)    #用super子类方法调用父类方法

    def do_homework(self):  
        super(Student, self).do_homework()         #子类方法和父类方法出现了同名的方法，会优先调用子类的方法   #super不但可以调用构造函数还可以调用实例方法
        print('english homework')

student1 = Student('schoolA','bobby',18)
student1.do_homework()
#print(student1.sum)
#print(Student.sum)      #子类继承了父类的类变量

#print(student1.name)
#print(student1.age)
#print(student1.school)
#student1.get_name()
