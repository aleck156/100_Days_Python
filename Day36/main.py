import requests

from Personal_Projects import API_KEYS as ak
STOCK_NAME = "TSLA"
COMPANY_NAME = 'Tesla'

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

# PARAMS
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': ak.STOCK_API_KEY
}

news_param = {
    'apiKey': ak.NEWS_API,
    'qInTitle': COMPANY_NAME
}

# STOCK
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]

yesterday_closing_price = float(yesterday['4. close'])
day_before_yesterday_closing_price = float(data_list[1]['4. close'])

difference = yesterday_closing_price - day_before_yesterday_closing_price

diff_percent = (difference / yesterday_closing_price) * 100
print(diff_percent)



if abs(diff_percent) > 1:
    news_response = requests.get(NEWS_ENDPOINT, params=news_param)
    news_response.raise_for_status()
    top_three_articles = news_response.json()['articles'][:3]
    for article in top_three_articles:
        print(f'Headline:\t\t{article["title"]}\n{article["description"]}\n')