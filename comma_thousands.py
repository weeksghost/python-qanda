'''
Question:
----

Implement the thousands_with_commas function, 
which should take an integer and return
a string representation of that integer
with commas separating groups of three digits.

Answer:
----
'''

def thousands_with_commas(i):
    s = '%d' % i
    groups = []

    # Run so long as input given are digits and there is at least one character
    while s and s[-1].isdigit():

        # Append integer from the *third-last (included) to the end
        groups.append(s[-3:])

        # Re-assign variable 's' from the *third-last integer (included) to the beggining
        s = s[:-3]

        '''
        Since list created will look like this ['789', '456', '123'] we need to reverse the order.
        Next we will concatinate 's' with commas and join the reversed output for groups forming our desired value.
        '''

    return s + ','.join(reversed(groups))


"""
Simple illustration of how slices work:

 +---+---+---+---+
 | 1 | 2 | 3 | 4 |
 +---+---+---+---+
 0   1   2   3   4
-4  -3  -2  -1

"""


if __name__ == '__main__':

    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'
    assert thousands_with_commas(-23432432434.34) == '-23,432,432,434'
    print '123456789 is returned as: %s' % thousands_with_commas(123456789)
