import datetime

TS = [1427769570.266099, 1427769191.268007, 1427774014.309288]


def timestamp_oldest():
  pts = []
  for tss in TS:
    frts = datetime.datetime.fromtimestamp(tss)
    pts.append(frts)
    pts.sort()
    oldest = min(pts)
  print(oldest)

  # OR

  print(datetime.datetime.fromtimestamp(sorted(TS)[0]))

timestamp_oldest()

# Treehouse Answer

"""
def timestamp_oldest(*args):
  pos = []
  for arg in args:
    frts = datetime.datetime.fromtimestamp(arg)
    pos.append(frts)
    pos.sort()
    oldest = min(pos)
  return oldest
"""

