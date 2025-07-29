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
person1 = Person("John", 40)
person1.introduce()

student1 = Student("Emma", 22, "Python Programming")
student1.introduce()
student1.study()
