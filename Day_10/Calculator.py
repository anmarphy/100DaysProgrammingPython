from calculator_functions import *

n1=int(input('What is your first number? '))
n2=int(input('What is your second number '))
print('Select one of the operators below: ')

operations={
    '+':add,
    '-':substract,
    '*':multiply,
    '/':division
}

for opt in operations:
    print(opt)

operation_user=input()

def custom_calculator(operation_user, n1, n2):
    calculation_function=operations[operation_user]
    result = calculation_function(n1, n2)
    return result

result=custom_calculator(operation_user, n1, n2)
print(f'{n1} {operation_user} {n2} = {result}')
continue_calculation=input('Do you want to continue? Yes or No ')

while continue_calculation=='Yes':
    print('Pick another operation: ')
    operation_user=input()
    n1=result
    n2=int(input('What is the new number? '))
    result=custom_calculator(operation_user, n1, n2)
    print(f'{n1} {operation_user} {n2} = {result}')
    continue_calculation=input('Do you want to continue? Yes or No ')

print('See you soon!')