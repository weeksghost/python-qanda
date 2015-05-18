#A small frog wants to get to the other side of the road.
#The frog is currently located at position X
#and wants to get to a position greater than or equal to Y.
#The small frog always jumps a fixed distance, D.
#Count the minimal number of jumps that the small
#frog must perform to reach its target.
#Write a function that, given three integers X, Y and D,
#returns the minimal number of jumps from position X to a
#position equal to or greater than Y.

#For example, given:
#
#  X = 10
#  Y = 85
#  D = 30
#the function should return 3, because the frog will be positioned as follows:
#after the first jump, at position 10 + 30 = 40
#after the second jump, at position 10 + 30 + 30 = 70
#after the third jump, at position 10 + 30 + 30 + 30 = 100

from random import randint

X = randint(1, 1000000000)
D = 3000000
Y = randint(1000000001, 2000000000)

#def solution(X, Y, D):
#    count = 0
#    while X < Y:
#        X += D
#        count += 1
#        if X >= Y:
#            print(count)

# Ideal solution

def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        print distance / D
    else:
        print distance / D + 1

#solution(randint(1, 10000000), randint(1, 300000), randint(1000001, 2000000))
solution(X, Y, D)
