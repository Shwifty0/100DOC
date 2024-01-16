import requests
from bs4 import BeautifulSoup
import smtplib

PRICE = 7.50
URL = "Amazon URL of the item you want to track"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")

price_of_product = float([item.text for item in soup.select("span.a-offscreen")][1][1:])
title_of_product = " ".join(soup.find("span", {"id" : "productTitle"}).text.strip().split(" ")[:3])


message_to_mail = f"Subject: Your Amazon Price Tracker\n\nThe price for the product: {title_of_product} has dropped. Check it out here:\n{URL}"
if price_of_product < PRICE:
    try:
        print("Setting up 'smtp' to send emails.")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            print("Setting up ttls...")
            connection.starttls()
            print("Attempting to log into account...")
            connection.login("YOUR EMAIL", password= "YOUR APP PASSWORD")
            print("Successful Login!")
            connection.sendmail(from_addr="ozairmohammad12@gmail.com",
                                                to_addrs="ozairmohammad12@gmail.com",
                                                msg=message_to_mail)
            print("Email has been sent.")
    except:
        pass
else:
    print("The price is still the same.")
        