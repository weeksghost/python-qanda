#!/usr/bin/python

def peak_traffic(path_to_file):

    test_cases = open(path_to_file, 'r')
    links = set(map(lambda test: tuple(test.strip()[28:].split()), test_cases))
    test_cases.close()

    cs = []
    for email in set([a for link in links for a in list(link)]):
      for c in cs:
        if all([(email, other) in links and (other, email) in links for other in c]):
          c.append(email)
      cs.append([email])

    print '\n'.join(sorted(map(lambda ls: ', '.join(sorted(ls)), filter(lambda ls: len(ls) >= 3, cs))))

peak_traffic('codeeval/peaktraffic.txt')
