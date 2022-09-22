#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# get the string representation
n = repr(number)
# access the last string
last_str = n[-1]
# convert the string to an integer
last_digit = int(last_str)
print("Last digit of {} is {}".format(number, last_digit), end=" ")
if last_digit > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0")
