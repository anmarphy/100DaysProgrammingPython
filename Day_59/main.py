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