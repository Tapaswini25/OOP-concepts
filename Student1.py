# class Car:
#     color ="Blue"
#     brand= "Mercedes"

# Car1= Car()
# print(Car1.color)
# print(Car1.brand)

class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks=marks

s1= Student("Joey", 98)
print(s1.name, s1.marks)

s2= Student("chase", 94)
print(s2.name, s2.marks)