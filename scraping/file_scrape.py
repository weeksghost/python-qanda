import re
import requests


symfile = open("scraping/companies.txt")
symbols = symfile.read()
newsymbols = symbols.split('\n')

index = 0
while index < len(newsymbols):
  url = 'http://finance.yahoo.com/q?s={}'.format(newsymbols[index])
  request = requests.get(url)
  htmltext = request.text
  regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
  pattern = re.compile(regex)
  price = re.findall(pattern, htmltext)

  print('The price of {} is {}'.format(newsymbols[index], price[0]))
  index += 1
