import math


def _sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return +1
    else:
        return 0


def root2(n):
    return n**0.5


def root3(n):
    return math.pow(abs(n), 1/3)*_sign(n)
