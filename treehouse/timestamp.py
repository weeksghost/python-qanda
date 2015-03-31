import datetime

TS = [1427769570.266099, 1427769191.268007, 1427774014.309288]


def timestamp_oldest():
  pts = []
  for tss in TS:
    frts = datetime.datetime.fromtimestamp(round(tss))
    pts.append(frts)
    pts.sort()
  #  oldest = str(min(pts))
  #  timeconv = datetime.datetime.strptime(oldest, '%Y-%m-%d %H:%M:%S')
  #print(timeconv)
    oldest = min(pts)
  print(oldest)

timestamp_oldest()


#def timestamp_oldest(*args):
#  now = datetime.datetime.now()
#  ts = round(now.timestamp())
#  frts = [datetime.datetime.fromtimestamp(ts)]
#  pos = []
#  for ts in frts:
#    pos.append(ts)
#    pos.sort()
#    oldest = str(min(pos))
#    timeconv = datetime.datetime.strptime(oldest, '%Y-%m-%d %H:%M:%S')
#  return timeconv
