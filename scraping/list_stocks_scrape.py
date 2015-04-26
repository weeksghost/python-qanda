import re
import requests


symbols = [
            "AAPL",
            "GOOG",
            "SPY",
            "NFLX",
            "CMG"
          ]

index = 0
while index < len(symbols):
  symlist = []
  for sym in symbols:
    sym.lower()
    symlist.append(sym.lower())
    url = 'http://finance.yahoo.com/q?s={}'.format(symlist[index])
    request = requests.get(url)
    htmltext = request.text
    regex = '<span id="yfs_l84_'+symlist[index]+'">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)

    print('The price of {} is {}'.format(symlist[index], price))
    index += 1
