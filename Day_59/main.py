## Dictionaries are mutable

friends_last_seen ={
    'Rolf' : 31,
    'Anne' : 7
}
print(id(friends_last_seen)) #this number 
friends_last_seen['Rolf'] = 5
print(friends_last_seen)

another_variable = friends_last_seen
print(id(another_variable))


#List are mutable
friends = ['Juan', 'Leo', 'M']
print(id(friends))
friends.append('Andres')
print(id(friends))


## Inmutable: integers, floats, strings, tuples

my_int = 5
print(id(my_int))
my_int = 6
print(id(my_int))


## Default value parameters. those arguments should be add the end of the funcion list of parameters.
accounts = {
    'checking' : 1234.40,
    'savings' : 3523.21
}

def add_balance(amount : float, name: str) -> float:
    accounts[name] += amount
    return accounts[name]

print(add_balance(100, 'checking'))

transactions = {
    (-30.0, 'checking'),
    (140.1, 'savings'),
    (250.0, 'savings'),
    (32.2, 'checking')
}

for transaction in transactions:
    add_balance(*transaction) #unpacking arguments for a tuple
print(accounts)


def create_account(name: str, holder: str, account_holder = None):
    if not account_holder:
        account_holder = []

    account_holder.append(holder)

    return {
        'name': name, 
        'main_account_holder': holder,
        'account_holders' : account_holder
    }    

a1 = create_account('checking', 'Jenn')
print(a1)

a2 = create_account('savings', 'Juan')
print(a2)


class User:
    def __init__(self, username, password):
        self.username = username, 
        self.password = password

users = [
    {'username' : 'rolf', 'password' : 'mamges'},
    {'username' : 'pilar', 'password' : '4dg3e3'}
]

user_objects = [User(data['username'], data['password']) for data in users]
print(user_objects)

user_objects = [User(**data) for data in users] #unpacking a dictionary
print(user_objects)


## queues

friends = ['Rolf' , 'Charlie', 'Anna']
friends.append('Jen')
print(friends)

friends.pop()
print(friends)
