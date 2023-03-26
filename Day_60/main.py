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