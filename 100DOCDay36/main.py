import requests
from datetime import datetime, timedelta 
from apik import STOCK_API_KEY, NEWS_API_KEY



stock_api_params = {
    "function":"TIME_SERIES_DAILY",
    'symbol': "TSLA",
    "apikey": STOCK_API_KEY
}

news_api_params = {
    "q":"Tesla Stock Price Today",
    "from":str((datetime.now() - timedelta(1))).split(" ")[0],
    "apiKey":NEWS_API_KEY
}

stocks_respone = requests.get(url='https://www.alphavantage.co/query', params=stock_api_params)
news_response = requests.get(url = "https://newsapi.org/v2/everything", params=news_api_params)

stocks_respone.raise_for_status()
stock_price = stocks_respone.json()
#print(stock_price)
print(f"{news_response.json()['articles']}")
yesterday = datetime.now() - timedelta(1)
db_yesterday  = yesterday - timedelta(1) - timedelta(1) - timedelta(1) - timedelta(1) - timedelta(1) 

yesterday_key, db_yesterday_key = str(yesterday).split(" ")[0], str(db_yesterday).split(" ")[0]


yest_cv = stock_price[yesterday_key]['4. close']
db_yest_cv = stock_price[db_yesterday_key]['4. close']

percent_diff = ((yest_cv - db_yest_cv) / ((yest_cv + db_yest_cv) / 2)) * 100