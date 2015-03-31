import datetime

TS = [1427769570.266099, 1427769191.268007, 1427774014.309288]

def timestamp_oldest():
  #now = datetime.datetime.now()
  #ts = round(now.timestamp())
  #frts = [datetime.datetime.fromtimestamp(ts)]
  #pos = []
  #for ts in frts:
  #  pos.append(ts)
  #  pos.sort()
  #  for p in pos:
  #    return p[0]
  pts = []
  for tss in TS:
    frts = datetime.datetime.fromtimestamp(round(tss))
    pts.append(frts)
    pts.sort()
    oldest = min(pts)
  # convert to strftime here

timestamp_oldest()
