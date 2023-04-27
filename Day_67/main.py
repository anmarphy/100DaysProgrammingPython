def add_all(a1, a2, a3, a4):
    return a1+a2+a3+a4

vals = (1,3,4,5)
print(add_all(*vals))

vals = {'a1' : 1, 'a2':3, 'a3':4, 'a4':5}
print(add_all(**vals))

def add_all(*args):
    return sum(args)

print(add_all(1,5,6,4))

def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'For {k} we have {v}')

print(pretty_print(user ='Marce', access_level='user'))

pretty_print(**{'day':'Thursday', 'class':'aerial'})
