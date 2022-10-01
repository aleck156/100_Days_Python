import requests

from Personal_Projects import API_KEYS as ak
STOCK_NAME = "TSLA"
COMPANY_NAME = 'Tesla, inc.'

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': ak.STOCK_API_KEY
}
res = requests.get(STOCK_ENDPOINT, params=stock_params)
res.raise_for_status()
data = res.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]

# data points
yesterday_closing_price = float(yesterday['4. close'])
day_before_yesterday_closing_price = float(data_list[1]['4. close'])

difference = yesterday_closing_price - day_before_yesterday_closing_price

diff_percent = (difference / yesterday_closing_price) * 100
print(diff_percent)

if diff_percent > 5:
    print('get news')