import requests
import os
import numpy as np

api_key = os.getenv("API_KEY")
parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "NVDA",
    "apikey" : api_key,
}

news_key = os.getenv("NEWS_KEY")
news_parameters = {
    "apiKey": "d40106b34aa54202886ec23c615ee9f1",
    "q": "Nvidia",
    "from": "2025-03-04",
    "to": "2025-03-04",
    "pageSize":10,
    "sortBy":"popularity"
}

STOCK_NAME = "NVDA"
COMPANY_NAME = "Tesla Inc"

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



news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
news_response.raise_for_status()
news = news_response.json()['articles']

# new_list = [expression for item in iterable if condition]

news_list = [news['title'] for news in news]
print(news_list)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.




#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

