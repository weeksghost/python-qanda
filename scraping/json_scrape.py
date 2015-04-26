import re
import requests
from pprint import pprint


request = requests.get('http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US')
htmltext = request.text
json = request.json()
pprint(json['last_price'])
