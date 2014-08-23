'''
The Fibonacci Sequence.

The first number of the sequence is 0, the second number is 1,
each subsequent number is equal to the sum of the previous two numbers
of the sequence itself, yielding the sequence 0, 1, 1, 2, 3, 5, 8, etc.

'''


def _fib():
    # Generate the Fibonacci numbers
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def Fib(startNumber, endNumber):
    '''
    Cycle through numbers and check that they verify
    using the given conditions
    '''
    for num in _fib():
        if num > endNumber:
            return
        if num >= startNumber:
            yield num


if __name__ == '__main__':

    for _ in Fib(1, 1000000):
        print _
