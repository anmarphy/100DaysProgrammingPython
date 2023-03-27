## Interesting Python Collections
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

device_temperature = [13.5, 14, 12, 12.4, 5.9, 12.4]
temperature_counter = Counter(device_temperature)
print(temperature_counter[12.4])


coworkers = [('Rolf', 'MIT'), ('Charlie', 'Oxford'), ('Rolf', 'Cambridge'), ('Peter', 'MIT')]
alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

print(alma_maters['Peter'])

alma_maters.default_factory = None
#print(alma_maters['Marce'])

my_company = 'Teclado'

coworkers = ['Jenn', 'Li', 'Charlie']
other_coworkers = [('Rolf', 'Apple'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)
print(coworker_companies)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0] ])
print(coworker_companies['Anna'])

o = OrderedDict() #In the order that they were inserted
o['Rolf'] = 6
o['Joao'] = 10
o['Andy'] = 4
print(o)

o.move_to_end('Rolf')
print(o)

o.popitem()
print(o)


##namedtuple
account = ('checking', 21343.2)
print(account[0])

Account = namedtuple('Accounts', ['name', 'balance'])
account = Account('checking', 3234) 
print(account)

##deque: Double ended queue

friends = deque(('Rolf', 'Charlie', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')
print(friends)


#### Exercise 19
def task1() -> defaultdict:
    """
    - create a `defaultdict` object, and its default value would be set to the string `Unknown`.
    - Add an entry with key name `Alan` and its value being `Manchester`.
    - Return the `defaultdict` object you created.
    """
    # you code starts here:
    data = defaultdict(lambda: 'Unknown')
    data['Alan'] = 'Manchester'
    return data

print(task1())


def task2(arg_od: OrderedDict):
    """
    - takes in an OrderedDict `arg_od`
    - Remove the first and last entry in `arg_od`.
    - Move the entry with key name `Bob` to the end of `arg_od`.
    - Move the entry with key name `Dan` to the start of `arg_od`.
    - You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
        and they won't be the first or last entry initially.
    """
    # you code starts here:
    arg_od.popitem()
    arg_od.popitem(False)
    # remember to remove start and end before moving Bob and Dan, otherwise they will be removed instead
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', False)


def task3(name: str, club: str) -> namedtuple:
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """
    # you code starts here:
    Player = namedtuple('Player', ['name', 'club'])
    player = Player(name, club)
    return player


def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    # you code starts here:
    arg_deque.pop()
    arg_deque.append(dq.popleft()) 
    arg_deque.appendleft('Zack')
