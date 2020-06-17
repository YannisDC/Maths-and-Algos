# if n is even -> n/2
# if n is odd -> 3n+1 (which becomes even so technically we can do 3n+1/2)
# does every number go to 1?

# count up and check if there is a number

import math

stack = [1]

def collatz_reverse(n, stack):
    stack.append(int(n))
    if math.modf(((n * 2) - 1) / 3)[0] == 0.0:
        collatz_reverse(((n * 2) - 1) / 3, stack)
    else:
        print(stack)
        return

def collatz_rev(n):
    return ((n * 2) - 1) / 3

def collatz_next(n):
    if (n % 2 == 0):
        return n / 2
    else:
        return (3 * n) + 1

def collatz(n, stack):
    stack.append(int(n))
    if n == 1:
        print(len(stack))
        print(stack)
        return

    if (n % 2 == 0):
        collatz(n / 2, stack)
    else:
        collatz((3 * n) + 1, stack)

print(collatz(27, []))

# every = 0
#
# odds = [x for x in range(1,100) if x % 2][(3**every) - 1::3**every]
# for odd in odds:
#     collatz_reverse(odd, [])
