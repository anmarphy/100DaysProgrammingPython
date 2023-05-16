from abc import ABCMeta, abstractmethod

class Animal:
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
         return 4   

class Monkey(Animal):
    def __init__(self, name):
        self.name = name
    
    def num_legs(self):
        return 2

monkus = Monkey('Monkus')
print(monkus.num_legs())

my_pets = [Dog('Mickey'), Monkey('Josh')]

for pet in my_pets:
    print(isinstance(pet,  Animal))
    print(pet.num_legs())
