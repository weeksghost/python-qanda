"""

Implement the thousands_with_commas function, 
which should take an integer and return
a string representation of that integer
with commas separating groups of three digits

"""

def thousands_with_commas(i):
    s = '%d' % i
    groups = []
    while s.isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + ','.join(reversed(groups))

if __name__ == '__main__':

    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'
