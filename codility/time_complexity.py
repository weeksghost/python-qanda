#Problem:
#You are given an integer n. Count the total of 1 + 2 + . . . + n.
import random


def solution(number):
    result = number * (number + 1) // 2
    return result


def test(got, expected):
    if type(got) == type(expected):
        prefix = 'OK'
    else:
        prefix = 'X'
    print('{} {} is not an integer: got {}'.format(
        prefix, repr(type(got)), repr(type(expected)))
    )

def main():
    rand = random.randint(0, 1000000)
    test(solution(rand), rand)


if __name__ == '__main__':
    main()
