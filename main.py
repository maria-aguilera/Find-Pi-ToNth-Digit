# Press Fn + Shift+F10 to execute it or replace it with your code.
"""Find PI to the Nth Digit - Have the user enter a number 'n' and print out pi to the 'nth' digit,i.e. to the number
of decimal places. Keep a limit of how far the program will go. """


import math, sys
import decimal

from math import factorial
from decimal import Decimal, getcontext
getcontext().prec = 1000

#decimal.getcontext().rounding = decimal.ROUND_FLOOR
#sys.setrecursionlimit(100000)

pi_digits = input('How many digits of pi would you like?')
n = int(pi_digits)


def cal(n):
    t = Decimal(0)
    pi = Decimal(0)
    denom = Decimal(0)



lim = 50
print('Reminder: Enter 0 to '+str(1) + ' only. To exit, enter "q" anytime.')

