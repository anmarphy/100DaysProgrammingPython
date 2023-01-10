from recipy import MENU

# TODO: Initial values
report={'water': 300,
 'milk': 200,
 'coffee': 100,
 'money': 0}



def coffee_machine():
    should_continue=True

    while should_continue==True:
        coffee_option= input('What would you like? (espresso/latte/cappuccino): ' )
        enough_ing = True
        # TODO: Validating ingredients
        def validate_resources(drink):
            counter = 0
            for ing in MENU[drink]['ingredients']:
                if MENU[drink]['ingredients'][ing] > report[ing]:
                    counter += 1
                    print( f' ❌ There is not enough {ing}. Choose another drink.')
                    coffee_machine()

            if counter == 0:
                for ing in MENU[drink]['ingredients']:
                    report[ing] -= MENU[drink]['ingredients'][ing]
                print(f'Enough ingredients ☕')

        validate_resources(coffee_option)



        # TODO: Process Money
        print('Please insert coins')
        q = int(input('Insert the quarters: '))
        d = int(input('Insert the dimes: '))
        n = int(input('Insert the nickels: '))
        p =  int(input('Insert the pennies: '))

        def validate_money(q, d, n, p):
            total = 0.25 * q + 0.10 * d + 0.05 * n + 0.01 * p


            if total >= MENU[coffee_option]['cost']:
                change = total - MENU[coffee_option]['cost']
                report['money'] += MENU[coffee_option]['cost']
                print(f'Here is your ☕ {coffee_option} with yours ${round(change, 2)} 💵 \nThe new report is:{report}')
            else:
                print(f'❌ Sorry, there is not enough money for the {coffee_option}')

        validate_money(q, d,n, p)
        other_drink=input('Do you want another drink? Yes or No ')
        if other_drink=='No':
            should_continue=False



# TODO: Print the report

coffee_machine()


