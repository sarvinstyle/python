# class - Object Oriented Programming

# class - object 

class Person:
    default_eye_color = "brown"
    def __init__(self , name ="unknown" , age = 0 ):
        self.name = name
        self.age = age

    def eat (self):
        print(f'{self.name} is eating')

    def __eq__(self , other):
        return self.name == other.name and self.age == other.age

# first_peson = Person("sarvin" , 30)
# second_peson = Person("sarvin" , 30)
# print(first_peson == second_peson)


# Inheritance 

class Animal:
    def __init__ (self , name , age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} eat")

class Mammal(Animal) :
    def __init__ (self , name , age , weight):
        super().__init__(name , age)
        self.weight = weight


    def walk (self):
        print("walk")

class Fish(Animal) :
    def swim(self):
        print("swim")


# cat = Mammal("cat" , 1 , '1kg')
# cat.eat()

# goldfish = Fish("goldfish" , 2)
# goldfish.eat()



class Grandparent:
    def feature1(self):
        return "Feature 1 from Grandparent"

class Parent(Grandparent):
    def feature2(self):
        return "Feature 2 from Parent"

class Child(Parent):
    def feature3(self):
        return "Feature 3 from Child"
    
# Multiple Inheritance

class Parent1:
    def comman(self):
        print("p1 common")
    def feature1(self):
        print("Feature 1")

class Parent2:
    def comman(self):
        print("cp2 common")
    def feature2(self):
        print("Feature 2")

class Child(Parent1, Parent2):

    def feature3(self):
        print("Feature 3")

child = Child()
child.comman()

# Abstract
from abc import ABC , abstractmethod

class Animal(ABC):
    def eat(self):
        return "Eat"
    
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class Sheep (Animal):
    def make_sound(self):
        return "Meow!"

a= Sheep()
    

# Polymorphism

class UIControl(ABC) :
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("textbox")

class DropDown(UIControl):
    def draw(self):
        print("dropdown")


def draw(control):
    control.draw()


text1 = TextBox()
d1 = DropDown()

draw(text1)
draw(d1)






