class Student:
    def _init_(self, name, age):
        self.__name = name  
        self.__age = age    
    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

student = Student("Alice", 20)

print("Name:", student.get_name())
print("Age:", student.get_age())

student.set_age(21)
print("Updated Age:", student.get_age())

student.set_age(-5)
