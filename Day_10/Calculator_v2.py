from calculator_functions import *

n1=int(input('What is your first number? '))
continue_calculation='Yes'

operations={
    '+':add,
    '-':substract,
    '*':multiply,
    '/':division
}


def custom_calculator(operation_user, n1, n2):
    calculation_function=operations[operation_user]
    result = calculation_function(n1, n2)
    return result


while continue_calculation == 'Yes':
    n2 = int(input('What is the number '))
    print('Select one of the operators below: ')
    for opt in operations:
        print(opt)

    operation_user = input()

    result = custom_calculator(operation_user, n1, n2)
    print(f'{n1} {operation_user} {n2} = {result}')
    n1=result
    continue_calculation = input('Do you want to continue? Yes or No ')
    print(f'Your previous number is {n1}')




print('See you soon!')