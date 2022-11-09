import math


def calculate_pi(numb):
    pi_rounded = round(math.pi, numb)
    return pi_rounded


num = int(input('Enter number of digits you want after the decimal of pi: '))

try:
    print(calculate_pi(numb))
except:
    print('Enter an integer!')
