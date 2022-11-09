"""Find PI to the Nth Digit - Have the user enter a number 'n' and print out pi to the 'nth' digit,i.e. to the number
of decimal places. Keep a limit of how far the program will go.

Purpose: Get the value of Pi to n number of decimal places

Module Dependencies:
- Math provides fast square rooting
- Decimal gives the Decimal data type (much better than Float)
- sys needed to set the depth of recursion

 """

import math, sys
from decimal import *

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(10000)


def factorial(n):
    """
    Return the Factorial of a number using recursion.
    Parameters
     n: number to get factorial of
    """
    if not n:
        return 1
    else:
        return n * factorial(n - 1)


def getIteratedValue(k):
    """
    Return the Iterations as given in the Chudnowsky Algorithim.
    k iterations gives k-1 decimal places; since we need k decimal places make iterations equal to k+1
    Parameters:
     k: Number of Decimal Digits to get
    """
    k = k + 1
    # Sets the precision of Digits (e.g. prec = 2 will return 2 digits)
    getcontext().prec = k
    sum = 0
    for k in range(k):
        first = factorial(6 * k) * (13591409 + 545140134 * k)
        down = factorial(3 * k) * (factorial(k)) ** 3 * (640320 ** (3 * k))
        sum += first / down
    return Decimal(sum)


def getValueOfPi(k):
    """
    Returns the calculated value of Pi using the iterated value of the loop
    and some division as given in the Chudnovsky Algorithm
    Parameters:
    k -- Number of Decimal Digits up to which the value of Pi should be calculated
    """
    iter = getIteratedValue(k)
    up = 426880 * math.sqrt(10005)
    pi = Decimal(up) / iter

    return pi


def shell():
    """
	Console Function to create the interactive Shell.
	Runs only when __name__ == __main__ that is when the script is being called directly
	No return value and Parameters
	"""
    print(
        "Welcome to Pi Calculator. In the shell below Enter the number of digits unto which the value of Pi should be calculated or enter quit to exit")

    while True:
        print(">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("You did not enter a number. Try again")
        else:
            print(getValueOfPi(int(entry)))


if __name__ == '__main__':
    shell()
