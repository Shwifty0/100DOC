import smtplib
import pandas as pd
import datetime as dt
import os
from random import choice

df = pd.read_csv("birthdays.csv")
data = df.to_dict()

today = dt.datetime.today()
month, day = today.month, today.day

MY_EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

letter_templates = os.listdir("letter_templates")

for i in range(len(data)):
    random_letter_template = choice(letter_templates)
    
    try:
        # 2. Check if today matches a birthday in the birthdays.csv
        if data["month"][i] == month and data["day"][i] == day:
            print(data["month"][i], month, data["day"][i], day)
            name  = data["name"][i]
            email = data["email"][i]
            
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            with open(f"letter_templates/{random_letter_template}", "r") as f:
                letter = f.read().replace("[NAME]", name)
                print(f"This is the letter that will be sent:\n'{letter}'")
            
            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject: Happy Birthday!\n\n{letter}")
                print("email has been sent")
    except KeyError:
        pass
        













