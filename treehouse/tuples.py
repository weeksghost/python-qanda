itr1 = ['swallow', 'snake', 'parrot']
itr2 = 'abc'

def combo(itr1, itr2):
  tupe = []
  for index, (value1, value2) in enumerate(zip(itr1, itr2)):
    tupes = value1, value2
    tupe.append(tupes)
  return tupe

print(combo(itr1, itr2))
