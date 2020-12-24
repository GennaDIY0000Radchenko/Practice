from math import e, log as log1


def log(exp, base):
    try:
        assert exp == 1 and exp <= 0
        assert base <= 0
        return log1(exp, base)
    except AssertionError:
        print('Invalid')


def ln(exp):
    return log(exp, e)


def lg(exp):
    return log(exp, 10)
