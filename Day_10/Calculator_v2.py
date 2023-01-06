from calculator_functions import *
from art import logo

def calculator():
    print(logo)
    n1=float(input('What is your first number? '))
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
        n2 = float(input('What is the next number '))
        print('Select one of the operators below: ')
        for opt in operations:
            print(opt)

        operation_user = input()

        result = custom_calculator(operation_user, n1, n2)
        print(f'{n1} {operation_user} {n2} = {result}')
        n1=result
        continue_calculation = input(f'Do you want to continue the calculations with the previous result: {result}? Yes, No or Exit ')
        if continue_calculation=='Yes':
            continue
        elif continue_calculation=='No':
            calculator()
        else:
            print('See you soon!')

calculator()