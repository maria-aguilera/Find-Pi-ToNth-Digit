# Press Fn + Shift+F10 to execute it or replace it with your code.
"""Find PI to the Nth Digit - Have the user enter a number 'n' and print out pi to the 'nth' digit,i.e. to the number
of decimal places. Keep a limit of how far the program will go. """


import math, sys
import decimal

decimal.getcontext().rounding = decimal.ROUND_FLOOR
sys.setrecursionlimit(100000)


lim = 50
print('Reminder: Enter 0 to '+str(1) + ' only. To exit, enter "q" anytime.')

