import requests
from datetime import datetime
import smtplib
import os

MY_LAT = 16.043859 # Your latitude
MY_LONG = 120.335190 # Your longitude

SUBJECT = "IT WORKED"

MESSAGE = "TIME TO WAKE UP"

MY_EMAIL = os.environ["email"]
MY_PASSWORD = os.environ["password"]

RECIPIENT = "cataptrial@yahoo.com"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

MY_LAT_UPPER = MY_LAT + 5
MY_LAT_LOWER = MY_LAT - 5

MY_LONG_UPPER = MY_LONG + 5
MY_LONG_LOWER = MY_LONG - 5

if iss_longitude < MY_LONG_UPPER and iss_longitude > MY_LONG_LOWER:
    if iss_latitude < MY_LAT_UPPER and iss_latitude > MY_LAT_UPPER:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(to_addrs=RECIPIENT, from_addr=MY_EMAIL, msg=f"Subject:{SUBJECT}\n\n"
                                                                        f"{MESSAGE}")
        connection.quit()
# else:
#     print("False")
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=MY_EMAIL, password=MY_PASSWORD)
# connection.sendmail(to_addrs=RECIPIENT, from_addr=MY_EMAIL, msg=f"Subject:{SUBJECT}\n\n"
#                                                                 f"{MESSAGE}")
# connection.quit()






#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



