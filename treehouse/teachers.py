# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!

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

print(most_classes(mdict))
