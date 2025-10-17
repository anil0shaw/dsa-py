class student:
    def_int_(self,name,age);
    self.name=name
    self.age=age
    
    def myfunc(self):
        print("hello is my name is"+self.name)
        print("hello is my age is"+self.age)
name=input("enter your name")
age=input("enter your age")
p1=student(name,age)
p1.myfunc()
print(p1.__module__)