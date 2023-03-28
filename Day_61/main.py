#Dates and Times in Python

from datetime import datetime, timezone, timedelta

print(datetime.now()) #naive time information, not inclide the timezone
print(datetime.now(timezone.utc)) #this is the standard to work with time
today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)
print(tomorrow)

print(tomorrow.strftime('%d-%m-%Y')) #string format

user_date = input('Enter date YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')
print(user_date)

#Timing your code
import time

def powers(limit):
    return [x**2 for x in range(limit)]


start = time.time()
powers(5000)
end =time.time()
print( end - start ) #basic calculation


def measure_runtime(func): #more generic calculation
    start = time.time()
    func()
    end = time.time()
    print(end - start)

measure_runtime(lambda: powers(5000))


##
import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))


## Regex: Regular Expressions
import re
"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""


def is_filename_safe(filename):
    # you only need to change the regular expression (regex) below
    regex = '^[a-zA-Z0-9][a-zA-Z0-9-_()]*\.(jpg|jpeg|png|gif)$'
    return re.match(regex, filename) is not None


##Loggin in Python
import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level=logging.DEBUG, 
                    filename='logs.txt')
logger = logging.getLogger(__name__)
logger.info('This is not show up')
logger.warning('This will')
logger.debug('This is a debug message')
logger.critical('This is a critical message')

'''
DEBUG
INFO
WARNING
ERROR
CRITICAL
'''

##Higher order functions
def greet():
    print('Hello')

def before_and_after(func):
    print('Before...')
    func()
    print('After')

print(before_and_after(greet))


movies = [
    {"name" : "The matrix", "director" : "Wachowski"}, 
    {"name" : "Amelie", "director" : "Jean-Pierre Jeunet" },
    {"name" : "The Irishman" , "director" : "Scoresese"}
]


def find_movie(expected, finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie



find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
movie = find_movie(looking_for, lambda movie: movie[find_by])
print(movie or 'No movies found')

