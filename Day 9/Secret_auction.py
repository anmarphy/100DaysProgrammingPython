import os

bid_continue='Yes'
bidders_info={}
max_bid=0
max_user=''

while bid_continue=='Yes':
    print('Welcome to the secre auction program')
    user=input('What is your name?')
    bid=int(input('What is your bid? $'))

    bidders_info[user]=bid

    more_bidders=input('Are there any other bidders? Type "Yes" or "No"')

    if more_bidders=='No':
        bid_continue='No'

        for i in bidders_info:
            if bidders_info[i]>max_bid:
                max_bid=bidders_info[i]
                max_user=i
        print(f'The highest bid was {max_bid} from {max_user}')

    elif more_bidders=='Yes':
        os.system('CLS')

    else:
        print('That is not a valid option')
        more_bidders = input('Are there any other bidders? Type "Yes" or "No"')

