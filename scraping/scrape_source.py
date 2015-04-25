import re
import requests


urls = ['http://broadway.com', 'http://google.com', 'http://yahoo.com']

index = 0
regex = '<title[^>]*>([^<]+)</title>'
pattern = re.compile(regex)

while index < len(urls):
  request = requests.get(urls[index])
  htmltext = request.text
  titles = re.findall(pattern, htmltext)
  print(titles)
  index += 1
