1.Given an integer n, print true if it is a power of three. Otherwise, print false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

#power of three
import math
n=int(input())

i=0

while True:
    if 3**i==n:
        print("True")
        break
    if 3**i>n:
        print("False")
        break
    i=i+1


