Given a number N, find the next perfect square greater than N.

Input Format:

Integer input from stdin.

Output Format:

Perfect square greater than N.

Example Input: 10

Output: 16

Code:

n=int(input())
c=1
while True:
  if (c*c)> n:
    print(c*c)
    break
  c=c+1
