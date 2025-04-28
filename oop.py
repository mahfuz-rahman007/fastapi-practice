class Animal:
    weight:int = 10

    def walk(self):
        print("Animal Walking")
    
    def eat(self):
        print("Animal Eating")

class Dog(Animal):
    leg:int = 4

    def bark(self):
        print("Dog Barking")

class Bird(Animal):
    leg:int = 2

    def fly(self):
        print("Bird Flying")

    def walk(self):
        print("Bird is Walking")

dog = Dog()
dog.bark()
dog.walk()
dog.eat()
print("====================")
bird = Bird()
bird.eat()
bird.walk()
bird.fly()