oldfile = open('scraping/symbols.txt', 'r')
newfile = open('threads/symbols2.txt', 'w')
result = [line.split() for line in oldfile]
for lines in result:
  for line in lines:
    print(line)
    newfile.write(line+'\n')
