
"""Find PI to the Nth Digit - Have the user enter a number 'n' and print out pi to the 'nth' digit,i.e. to the number
of decimal places. Keep a limit of how far the program will go. """

from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 1000 # Sets the precision of digits e.g. `prec = 2`, will return 2 digits

#decimal.getcontext().rounding = decimal.ROUND_FLOOR
#sys.setrecursionlimit(100000)

pi_digits = input('How many digits of pi would you like?')
n = int(pi_digits)


def calcPi(n):
    """
    Prints out the digits of PI until it reaches the given limite
    :param n:
    :return:
    """

    # Assigning t, pi and denom a 0 in decimal format
    top = Decimal(0)
    pi = Decimal(0)
    denom = Decimal(0)

    for k in range(n):
        top = ((-1)**k)*(factorial(6*k))*(13591409+(545140134*k))
        denom = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(top)/Decimal(denom)
        pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
        pi = 1/pi

        return round(pi,n)






print(calcPi(150))

#lim = 50
#print('Reminder: Enter 0 to '+str(1) + ' only. To exit, enter "q" anytime.')

