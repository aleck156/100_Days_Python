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

import smtplib
import datetime as dt
import random

MY_EMAIL = 'gmail@test.com'
PASS = 'TSET321'

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open('quotes.txt') as quote_file:
        all_qoutes = quote_file.read().split('\n')
        quote = random.choice(all_qoutes)
        print(quote)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f'Subject:Daily Motivation\n\n{quote}'
        )
