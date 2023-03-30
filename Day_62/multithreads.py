#Sequential running
import time

def ask_user():
    start = time.time()
    user_input = input('Enter your name:')
    greet = f'Hello {user_input}'
    print(greet)
    print(f'ask user, {time.time() - start} ')

def complex_calculation():
    start = time.time()
    print('Starting calculation...')
    [x**2 for x in range(20000000)]
    print(f'complex calculation, {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')


##### Asynchronous
from threading import Thread

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print(f'Total time {time.time() - start}')