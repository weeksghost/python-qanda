# Based on https://www.youtube.com/watch?v=SFas42HBtMg
# Page Spider

import urlparse
import requests
from bs4 import BeautifulSoup

url = 'http://broadway.com'

urls = [url]
visted = [url]

while len(urls) > 0:
  try:
    request = requests.get(urls[0])
    htmltext = request.text
  except:
    print(urls[0])
  soup = BeautifulSoup(htmltext)

  urls.pop(0)
  print(str(len(urls)) + ' links checked out okay')

  for tag in soup.findAll('a', href=True):
    tag['href'] = urlparse.urljoin(url, tag['href'])
    if url in tag['href'] and tag['href'] not in visted:
      urls.append(tag['href'])
      visted.append(tag['href'])
  for link in visted:
    response = requests.get(link)
    if response.status_code != 200:
      print('[%s] %s' % response.status_code, link)
