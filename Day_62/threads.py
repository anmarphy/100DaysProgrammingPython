#Sequential running
import time
from concurrent.futures import ThreadPoolExecutor

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

start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

pool.shutdown()
print(f'Two threads total time: {time.time() - start }')
