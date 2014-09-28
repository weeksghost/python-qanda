'''

Determine if any given integer
(generated at random) is a prime number.

'''

from random import randint

def is_prime(number):
    # Since a prime number can't be lower that 2...
    if number < 2:
        return False
    else:
        '''
        If arg 'number' is prime
        no other number should go into it evenly
        besides 1 and itself.

        For example, 97 is a prime number.
        If we pass 97 as our arg, below we
        create a range of numbers
        2 through 95. If the remainder from
        dividing any number within the specified
        range i.e. any number betwween 2 and 96
        equals 0 then the number is not prime and
        our funtion returns False.
        '''
        for _ in range(2, number - 1):
            if number % _ == 0:
                return False
    return True


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

print get_primes(randint(2, 8999))
