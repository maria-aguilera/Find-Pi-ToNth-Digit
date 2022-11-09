"""Find PI to the Nth Digit - Have the user enter a number 'n' and print out pi to the 'nth' digit,i.e. to the number
of decimal places. Keep a limit of how far the program will go. """

from IPython.display import clear_output
import math


def find_num(n):
    """
    This function turns the gloat pi into a string to be able to iterate through it, and prints pi up to that decimal
    point.
    :param n:user input up to 17 digits
    :return: calls function to printout pi to "n" decimal points
    """
    s = str(math.pi)
    for i in s[n]:
        print(s[:n + 2])


def dec_pi():
    """
    This is the pi generator that takes a user input up ot 17 digits and then calls out the function "find_num()" to
    prints out pi to that number's decimal point :return:
    """
    print('Welcome to Pi Decimal Generator!')

    while True:
        try:
            s = int(input('Please enter a number to generate pi to that decimal point'))
            clear_output()

            if s <=17:
                find_num(s)
            else:
                print('Sorry, too many digits! Try a number 17 or below')
        except ValueError:
            print('Sorry input must be an integer. Please try again')

        else:
            break
