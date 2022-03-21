import random


def power(a, b):

    res = a
    while(b > 1):
        b = b//2
        if (b % 2):
            res *= res
        else:
            res *=

    return res


print(power(7, 8))
print(pow(7, 8))
