## generators and iterators

def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1
g = hundred_numbers()
print(next(g))
print(next(g))
print(list(g))

def prime_generator(bound):
    # your code starts here (delete the pass):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n

m = prime_generator(20)
print(next(m))
print(list(m))

