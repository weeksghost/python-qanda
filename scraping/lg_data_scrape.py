import re
import requests


symlist = open('scraping/companies.txt').read()
symlist = symlist.split('\n')

for sym in symlist:
  r = requests.get('http://bloomberg.com/markets/chart/data/1D/{}:US'.format(
                    sym)
                  )
  json = r.json()
  data = json['data_values']
  for point in data:
    print('symbol {} time {} price {}'.format(sym, point[0], point[1]))
