import re
import requests
from threading import Thread


def thread(url):
    base = 'http://finance.yahoo.com/q?s='+sym
    regex = '<span id="yfs_l84_'+url.lower()+'">(.+?)</span>'

    print(url)
    #print(base)

#    pattern = re.compile(regex)
#    r = requests.get(base)
#    htmltext = r.text
#    results = re.findall(pattern, htmltext)
#    print('The price of {} is {}'.format(url, results))

symlist = open('threads/symbols2.txt').read()
symlist = symlist.replace(' ', '').strip('\n').split(',')

#print(symlist)

threadlist = []

for sym in symlist:
  needle = Thread(target=thread,args=(sym,))
  needle.start()
  threadlist.append(needle)

for pin in threadlist:
  pin.join()
