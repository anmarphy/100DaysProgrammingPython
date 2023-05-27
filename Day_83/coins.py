def calculate_change(amount):
    change = {}

    denominations = [('quarters', 25), ('dimes', 10), ('nickels', 5), ('pennies', 1)]

    for denomination_name, denomination_value in denominations:
        num_denominations = amount // denomination_value
        amount %= denomination_value
        change[denomination_name] = num_denominations

    return change

# Example usage
amount = 37
change = calculate_change(amount)
print(change)
