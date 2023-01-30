import datetime as dt
import random
import pandas as pd

##################### Extra Hard Starting Project ######################
my_email=''

# 1. Update the birthdays.csv
today=(dt.datetime.now().month, dt.datetime.now().day)

# 2. Check if today matches a birthday in the birthdays.csv
birthdays=pd.read_csv('birthdays.csv')
birthdays['birthday']=birthdays.apply(lambda x: (x['month'], x['day']), axis=1)
birthday_dic=birthdays.to_dict('records')

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for i in range(len(birthday_dic)):
    if today == birthday_dic[i]['birthday']:
        birthday_person=birthday_dic[i]
        file_path=f'letter_templates/letter_{random.randint(1,3)}.txt'
        with open(file_path) as file_letter:
            contents=file_letter.read()
            contents=contents.replace('[NAME]', birthday_person['name'])



# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=birthday_person['email'],
                        msg=f"Subject: Happy Birthday {birthday_person['name']}!! \n \n {contents}")
    connection.close()
