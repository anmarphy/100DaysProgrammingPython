## *args: unspecified number of arguments
def add(*args):
    suma=0
    for n in args:
        suma+=n
    return suma

print(add(3,4,5))

## **kwarg: Keyworded Arguments

def calculate(n,**kwargs):
    n+=kwargs['add']
    n*=kwargs['multiply']
    print(n)

calculate(4, add=2, multiply=4)

class Car:
    def __init__(self, **kw):
        self.make=kw.get('make')
        self.model=kw.get('model')

my_car=Car(make='Mercedez Benz', model='Gla 1.6')
print(my_car.model)

car=Car()

