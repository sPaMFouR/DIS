import math
import sys
import os

# print("Hello", "World")
# print("Hello", "World", sep=":")
#
# # Python 3 has Python Functions (Python 2 Has Print Statements)
# # from __future__ import print_function (For Using Python Function In Python 2)
#
# # Python Is An Interpreter (Compiles Line By Line Code To A 'Byte' Code)
#
# # Integers Can Be Very Long In Python (Would Result In Overflow Errors In C)
#
# a = 32
# b = a ** 234
#
# x = 45
# y = math.cos(math.pow(math.sqrt(math.radians(x)), 2.4))
#
# # Complex Numbers
# c = 3 + 4j
# print(c ** 2)
# print(c.real)
# print(c.imag)
#
# # Syntax Error
# # print('John's Computer)
#
# print('John\'s Computer')
# print("John's Computer")
#
# attempt = 1
# input_value = 2.42
# final_result = 24.4242424242
# output = """
# Attempt No. %d
# --------------
# Tried Input Value: %6.3f
#   Obtained Answer: %6.3f
# """ % (attempt, input_value, final_result)
#
# output1 = """
# Attempt No. {0:d}
# --------------
# Tried Input Value: {1:6.3f}
#   Obtained Answer: {2:6.3f}
# """.format(attempt, input_value, final_result)
#
#
# print(output)
# print(output1)


# numbers = []
# while True:
#     user_input = input("Enter The Number: ").lower()
#     if user_input != 'stop':
#         numbers.append(float(user_input))
#     else:
#         break
#
# mean = sum(numbers) / len(numbers)
# print("Mean Is {0}".format(mean))


# In Python 2, Range would directly give a list. In Python 3, Range should be requested for a list - list(range(10))

num_list = [43, 23, 12, 34]

for i, num in enumerate(num_list):
    print(i, num)

print(sys.argv)


# Tuple Example

t = 1, 2, 3, 4
print(type(t))


def get_mean(num1, *nums):
    nums = list(nums)
    nums.insert(0, num1)
    total = 0
    for number in nums:
        total += number
    return total / len(nums)


def highly_flexible(*args, **kwargs):
    print(args)
    print(kwargs)

highly_flexible(1, 2, 3, 4, 5, name='Avinash', designation='SRF')


def make_function(n):
    def fun(x):
        return x**n
    return fun

f = make_function(3)
print(f(4))


import math

alist = [1, 2, 3, 4, 4]
aLog10 = list(map(math.log10, alist))
print(aLog10)


def filter_function(x):
    if x < 2:
        return True
    else:
        return False

aSub = list(filter(filter_function, alist))
print(aSub)

a = [1, 2, 4, 5]
# b = a  # B Just Points To The Memory Location Of A
# b = a[:]  # This Expression creates A New list B (Independent of Modifications In A)

