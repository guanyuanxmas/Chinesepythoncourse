#面向对象
#有意义的面向对象的代码
#类 = 面向对象
#类，对象
#实例化
#类最基本的作用：封装
class Student():
    name = ''
    age = 0

    def print_file(self):  
        print('name:' + self.name)
        print('age:' + str(self.age))

student = Student()
student.print_file()

""" 
函数与方法的区别：

函数和方法的理解：函数在模块下建议叫函数，函数在类里面建议叫方法变量在模块下建议叫变量，变量在类里面建议叫数据成员。 
"""




