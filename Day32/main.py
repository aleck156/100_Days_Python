# SEND EMAIL + DATETIME module
# import smtplib
#
# my_email = 'test@gmail.com'
# password = 'test1234'
#
# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs='gmail@test.com', msg='Hello worls')
# connection.close()

# import datetime as dt
# import pandas
#
# now = dt.datetime.now()
# print(now)
#
# date_of_birth = dt.datetime(year=1984, month=4, day=19)
# print(date_of_birth)
#
# quotes = pandas.read_csv('./quotes.txt', sep="-")
# print(quotes)


# if weekday == 6:
#     with open('quotes.txt') as quote_file:
#         all_qoutes = quote_file.read().split('\n')
#         quote = random.choice(all_qoutes)
#         print(quote)
#
#     with smtplib.SMTP('smtp.gmail.com') as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, PASS)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg=f'Subject:Daily Motivation\n\n{quote}'
#         )


import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = 'gmail@test.com'
PASS = 'TSET321'
HOST = 'smtp.gmail.com'

today_tuple = (dt.datetime.now().month,dt.datetime.now().day)
birthdays = pd.read_csv('./birthdays.csv')

birthdays_dict = {(data_row['month'], data_row['day']):data_row for (index, data_row) in birthdays.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f'./letter_templates/letter_{random.randint(1,3)}.txt'
    birthday_person = birthdays_dict[today_tuple]
    with open(file_path) as file:
        new_text = file.read().replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP(HOST) as connection:
        connection.starttls()
        connection.login()
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person['email'],
            msg=new_text
        )


with open('./quotes.txt', mode='r') as quotes_file:
    quotes = quotes_file.read().split('\n')
    # quotes_dict = {
    #     {
    #         'Quote':elem.splot,
    #         'Author:'
    #     }
    #     for elem in quotes
    # }
    daily_quote = random.choice(quotes)
    print(daily_quote)




