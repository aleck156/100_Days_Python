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
import pandas as pd

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    pass