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


# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                self.start += 1
                return n
        raise StopIteration()

print(PrimeGenerator(5).__next__())

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0
    
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self

first_100 = FirstHundredGenerator ()
print(first_100)


'''class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()
    
print(sum(FirstHundredIterable()))'''

for i in FirstHundredGenerator():
    print(i)

## Buildig functions: filter, map, any, all

friends = ['Joha', 'Pau', 'Pablo', 'Pili']

def start_with_p(friends):
    return friends.startswith('P')

start_with_p = filter(start_with_p, friends)
#print(list(start_with_p))
print(next(start_with_p))
print(next(start_with_p))

another_starts_p = (n for n in friends if n.startswith('P'))
print(list(another_starts_p))


friends_lower = map(lambda x: x.lower(), friends)
print(list(friends_lower))

print(list(friend.lower() for friend in friends)) #This is better option

friends = [
    {
    'name' : 'Rolf', 
    'city' : 'Washington'
    }, 
    {
    'name' : 'Ana', 
    'city' : 'San Francisco'
    },
    {
    'name' : 'Patrick',
    'city' : 'San Francisco'
    }
]

your_location = input('Where are you?')
friends_nearby = [ friend['name'] for friend in friends if friend['city'] == your_location]
print(friends_nearby)

if any(friends_nearby):
    print('You are not alone')


