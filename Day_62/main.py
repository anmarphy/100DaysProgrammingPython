#multiprocessing
import time
from multiprocessing import Process

def ask_user():
    start = time.time()
    user_input = input('Enter your name:')
    greet = f'Hello {user_input}'
    print(greet)
    print(f'ask user, {time.time() - start} ')

def complex_calculation():
    start = time.time()
    print('Starting calculation...')
    [x**2 for x in range(2000000)]
    print(f'complex calculation, {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')

#Processes
process = Process(target=complex_calculation)
process2 = Process(target=complex_calculation)

if __name__ == "__main__":
    process.start()
    process2.start()
    start = time.time()
    process.join()
    process2.join()

print(f'Two process total time {time.time() - start}')

