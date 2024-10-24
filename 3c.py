class Animal:
    def _init_(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks.")

animal = Animal("Some animal")
animal.sound()  
dog = Dog("Buddy")
dog.sound()
