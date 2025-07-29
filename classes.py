# 1. Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# 2. Child class Student
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}.")

# --- Test Calls ---
name = input("Enter person's name: ")
age = int(input("Enter person's age: "))
person1 = Person(name, age)
person1.introduce()
#---- stud calls ----
student_name = input("Enter student's name: ")
student_age = int(input("Enter student's age: "))
course = input("Enter student's course: ")
student1 = Student(student_name, student_age, course)
student1.introduce()
student1.study()
