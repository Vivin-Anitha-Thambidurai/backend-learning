"""
inheritance_and_polymorphism.py
--------------------------------
This file explains:
1. Inheritance
2. Method overriding
3. super()
4. Polymorphism
"""

# 1️⃣ Base (Parent) class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound")


# 2️⃣ Child class – Dog (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


# 3️⃣ Child class – Cat (inherits from Animal)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")


# 4️⃣ Using inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()


# 5️⃣ Using super()
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Name: {self.name}, Salary: £{self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        # Call parent constructor
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        print(
            f"Name: {self.name}, Salary: £{self.salary}, Department: {self.department}"
        )


manager = Manager("Vivin", 50000, "Engineering")
manager.get_details()


# 6️⃣ Polymorphism example
def make_animal_speak(animal):
    animal.speak()


make_animal_speak(dog)
make_animal_speak(cat)


# 7️⃣ Entry point check
if __name__ == "__main__":
    print("Inheritance and polymorphism example executed directly.")
