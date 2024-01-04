import requests
from datetime import datetime, timedelta 
from apik import STOCK_API_KEY, NEWS_API_KEY, TWILIO_AUTH_TOKEN, TWILIO_SID
from twilio.rest import Client


stock_api_params = {
    "function":"TIME_SERIES_DAILY",
    'symbol': "TSLA",
    "apikey": STOCK_API_KEY
}



stocks_respone = requests.get(url='https://www.alphavantage.co/query', params=stock_api_params)


stocks_respone.raise_for_status()
stock_price = stocks_respone.json()['Time Series (Daily)']


yesterday = datetime.now() - timedelta(1)
db_yesterday  = yesterday - timedelta(1) 

yesterday_key, db_yesterday_key = str(yesterday).split(" ")[0], str(db_yesterday).split(" ")[0]


yest_cv = stock_price[yesterday_key]['4. close']
db_yest_cv = stock_price[db_yesterday_key]['4. close']

percent_diff = ((float(yest_cv) - float(db_yest_cv)) / ((float(yest_cv) + float(db_yest_cv)) / 2)) * 100

up_down = None

if percent_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"



if abs(percent_diff) > 4:
    news_api_params = {
    "q":"TESLA",
    "from":str((datetime.now() - timedelta(1))).split(" ")[0],
    "searchIn": "title",
    "language":"en",
    "sortBy":"popularity",
    "apiKey":NEWS_API_KEY
    }

    news_response = requests.get(url = "https://newsapi.org/v2/everything", params=news_api_params)
    for article in news_response.json()['articles'][:3]:        
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=f"TSLA: {round(abs(percent_diff), 2)}{up_down}%\nHeadline:{article['title']}\nBrief:{article['description']}",
            from_= '+16179345452',
            to="+923130460101"
        )
    