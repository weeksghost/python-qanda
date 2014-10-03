"""Write a program that prints the numbers from 1 to 100.
But for multiples of three print 'Fizz' instead of the number.
For the multiples of five print 'Buzz'.
For numbers which are multiples of both three and five print 'FizzBuzz'."""

from random import randint

num = randint(1, 100)

def fizzbuzz(num):
  for x in range(1, 101):
    print x


def main():
  fizzbuzz(num)

if __name__ == '__main__':
  main()
