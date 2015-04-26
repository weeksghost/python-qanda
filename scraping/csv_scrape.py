import re
import requests


#request = requests.get('http://www.google.com/finance?q=AAPL')
#htmltext = request.text
#regex = '<span id="ref_[^.]*_l">(.+?)</span>'
#pattern = re.compile(regex)
#results = re.findall(pattern, htmltext)

symfile = open("scraping/companies.txt")
symbols = symfile.read()
newsymbols = symbols.split('\n')

index = 0
while index < len(newsymbols):
  url = 'http://www.google.com/finance/getprices?q={}&x=NASD&i=10& \
                    p=25m&f=c&df=cpct&auto=1&ts=1430017419614& \
                    ei=qlM8VdHZEeSCsQfL2IHIDA'.format(newsymbols[index])

  request = requests.get(url)
  htmltext = request.text
  print(type(htmltext.split()[-1]))
  #if htmltext.split()[-1] != type(int):
  #  pass
  #print(htmltext.split()[-1])
  index += 1
