from bs4 import BeautifulSoup
import requests
import re
from time import sleep
from collections import Counter
from nltk.corpus import stopwords
import pandas
#%maplotlib inline


def text_cleaner(website):
    try:
        site = requests.get(website)
        content = site.text
    except:
        raise Exception("Website not found!")

    soup_obj = BeautifulSoup(content)

    for script in soup_obj(["script", "style"]):
        script.extract()
    text = soup_obj.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))


    def chunk_space(chunk):
        chunk_out = chunk + ' '
        return chunk_out

    text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode('utf-8')

    try:
        text = text.decode('unicode_escape').encode('ascii', 'ignore')
    except:
        return

    text = re.sub("[^a-zA-Z.+3]"," ", text)
    text = text.lower().split()
    stop_words = set(stopwords.words("english"))
    text = [w for w in text if not w in stop_words]
    text = list(set(text))
    return text

text_cleaner("http://www.workbridgeassociates.com/tech-jobs/new-york-ny/other/lead-qa-test-engineer/224196")