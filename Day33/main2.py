from datetime import datetime
import requests
import smtplib
import time

MY_LAT = 50.06143
MY_LON = 19.93658
ISS_URL = 'http://api.open-notify.org/iss-now.json'
SUN_URL = 'https://api.sunrise-sunset.org/json'
MY_EMAIL = 'gmail@test.com'
MY_PASS = 'TSET4321'

def is_iss_overhead():
    res = requests.get(url=ISS_URL)
    res.raise_for_status()

    data = res.json()
    iss_longitude = data['iss_position']['longitude']
    iss_latitude = data['iss_position']['latitude']

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LON - 5 <= iss_longitude <= MY_LON + 5:
        return True
    return False

def is_night():
    parameter = {
        'lat': MY_LAT,
        'lng': MY_LON,
        'date': 'today',
        'formatted': 0
    }

    res = requests.get(SUN_URL, parameter)
    res.raise_for_status()
    data = res.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(":")[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    return False

while True:
    time.sleep(3600)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject:ISS is visible tonight\n\nYeah, right ...'
        )


#
# iss_position = (longitude, latitude)
# print(iss_position)

# if res.status_code == 400:
#     raise Exception('That resource does not exist')
# elif res.status_code == 401:
#     raise Exception('Yout are not authorized to access this data')


