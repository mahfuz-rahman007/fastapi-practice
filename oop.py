class Animal:
    def __init__(self, animal, weight=10, color='black'):
        self.__animal = animal 
        self.weight = weight
        self.color = color

    def walk(self):
        print(f"{self.__animal} is Walking")
    
    def prop(self):
        print(f"{self.__animal} is weight {self.weight} and color is {self.color}")

class Dog(Animal):
    
    def __init__(self, weight=10, color='black'):
        super().__init__(animal='Dog', weight=weight, color=color)

    def bark(self):
        print("Dog is Barking")

class Bird(Animal):
    def __init__(self, weight=10, color='black'):
        super().__init__(animal="Bird", weight=weight, color=color)

    def fly(self):
        print("Bird Flying")

dog = Dog(20, "Brown")
dog.prop()
dog.bark()
dog.walk()
print("====================")
bird = Bird(5, "White")
bird.prop()
bird.walk()
bird.fly()