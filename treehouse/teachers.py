#http://teamtreehouse.com/library/python-collections/dictionaries/teacher-stats

from pprint import pprint

mdict = {

    'Andrew Chalkley': ['Ruby Basics'],
    'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
    'Kenneth Love': ['Python Basics', 'Python Collections'],
    'Pasan Premaratne': ['']
}


def most_classes(mdict):
  max_count = len(max(mdict.values()))
  for key, values in mdict.items():
    current_count = len(values)
    if current_count == max_count:
      return key

def most_classes(mdict):
  current_count = []
  max_count = 0
  for key in mdict:
    current_count.append(len(mdict[key]))
  for val in current_count:
    if val > max_count:
      max_count = val
  for key in mdict:
    if max_count == len(mdict[key]):
      return key

def num_teachers(mdict):
  return len(mdict.keys())

def stats(mdict):
  lst = []
  for key in mdict:
    name = key
    classes = len(mdict[key])
    lst.append([name, classes])
  return lst

def courses(mdict):
  all_courses = []
  for courses in mdict.values():
    for course in courses:
      all_courses.append(course)
  return all_courses

pprint(most_classes(mdict))
pprint(num_teachers(mdict))
pprint(stats(mdict))
pprint(courses(mdict))
