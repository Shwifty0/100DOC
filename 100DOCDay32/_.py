import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "ozairmohammad12@gmail.com"
MY_PASSWORD = "zdwdjadpqzggkrgy"


print("Connection made successfully")

now = dt.datetime.now()
day = now.weekday()

if day == 6:        
    with open("quotes.txt", mode="r", encoding="utf-8",) as f:
        quotes = f.readlines() 
        quote_to_send = choice(quotes)#.encode("ascii")#.decode("utf-8")
    print(quote_to_send)
    print(f"Subject: Your Daily Motivational Quote\n\n{quote_to_send}")
    message = f"Subject: Your Daily Motivational Quote\n\n{quote_to_send}"
    
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        print("Logged in successfully")
        
        connection.sendmail(from_addr=MY_EMAIL, to_addrs= MY_EMAIL, msg=message.encode("ascii", "ignore"))
        print("Email has been sent.")