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

print(res.json())