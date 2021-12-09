class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("Hello my age is " + str(self.age))

p1 = Person("John", 36)
p1.myfunc()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    print("Hello my age is " + str(abc.age))

p1 = Person("John", 36)
p1.myfunc()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

class Student():
    name = ''
    age = 0
    
    def print_file(self):
        print('name:' +  self.name)
        print('age:' + str(self.age))
        
student = Student()
student.print_file()



