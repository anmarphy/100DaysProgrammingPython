import smtplib
import datetime as dt
import random

my_email=''
password=''
now=dt.datetime.now()
weekday=now.weekday()

if weekday == 0:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs='anaer@gmail.com',
                        msg=f'Subject:Monday motivation \n \n {quote}')
    connection.close()