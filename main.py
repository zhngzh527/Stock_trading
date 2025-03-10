import requests
from dotenv import load_dotenv
import os
import numpy as np
from ui import Ui

load_dotenv()
STOCK_NAME = "NVDA"
COMPANY_NAME = "Nvidia"

api_key = os.getenv("API_KEY")
parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "NVDA",
    "apikey" : api_key,
}

news_key = os.getenv("NEWS_KEY")
news_parameters = {
    "apiKey": news_key,
    "q":COMPANY_NAME ,
    "from": "2025-03-04",
    "to": "2025-03-04",
    "pageSize":3,
    "sortBy":"popularity"
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(url=STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

#---------GET THE lAST CLOSING PRICE-----------#
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#---------GET THE DAY BEFORE YESTERDAY CLOSING PRICE-----------#
the_day_before_yesterday_data = data_list[1]
the_day_before_yesterday_closing_price = the_day_before_yesterday_data["4. close"]
print(the_day_before_yesterday_closing_price)

#------------------------GET THE % DIFFERENCE -------------------#
def percentage(x, y):
    price_changed = 100 *(abs(float(x) - float(y))
                          / float(x))
    round_num = np.around(price_changed, 2)
    return str(round_num) + "%"

difference = percentage(yesterday_closing_price,the_day_before_yesterday_closing_price)
print(difference)

#------------------------GET THE NEWS------------------------------#

news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
news_response.raise_for_status()
news = news_response.json()['articles']

# new_list = [expression for item in iterable if condition]

news_list = [news['title'] for news in news]
print(news_list)

app = Ui()
