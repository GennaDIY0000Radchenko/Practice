import numpy as np
import math


def print_matrix(m):
    '''
    Виводить матрицю, що складається з цифр
    Між цифрами друкує подвійний пробіл
    На початку та в кінці рядка друкує "|"
    '''
    print("|", sep="", end="")
    for i in range(0, len(m) ** 2):
        print(m[i // len(m)][i % len(m)], end='')
        if i == len(m) ** 2 - 1:
            print("|")
        elif i % len(m) == len(m) - 1:
            print('|', "\n|", sep="", end="")
        else:
            print('  ', end='')


def random_matrix(dim):
    '''
    Створює квадратну матрицю з випадковими цифрами в комірках
    '''
    m = np.random.randint(10, size=(dim, dim))
    return m


def factorial(dim):
    '''
    Повертає факторіал числа
    '''
    r = 1
    for i in range(1, dim + 1):
        r *= i
    return int(r)


def f_permutations(dim):
    '''
    Повертає список із усіх можливих перестановок цифр від 1 до dim
    без повторень, від найменшого до найбільшого
    усі значення зберігаються в строковому типі
    '''
    numbers = [int(i) for i in range(1, dim + 1)]
    bad_num = [str(i) for i in range(dim + 1, 10)]
    bad_num.append(str(0))
    first = 0
    last = 0
    for i in range(0, dim):
        first += numbers[i] * (10 ** (dim - i - 1))
        last += numbers[i] * (10 ** i)
    r = []
    for i in range(first, last + 9, 9):
        c = 0
        i = str(i)
        if len(set(i)) == len(i):
            for a in range(0, len(i)):
                if i[a] in bad_num:
                    c = 1
            if c == 0:
                r.append(str(i))
    return r


def f_inversion(dim, permutations):
    '''
    Повертає список з кількостями інверсій в кожному числі зі списку permutations
    зберігається в тому ж порядку
    усі значення зберігаються в цілочисленному форматі
    '''
    list1 = []
    for a in range(0, len(permutations)):
        count = 0
        for i in range(0, dim - 1):
            for b in range(i + 1, dim):
                if int(permutations[a][i]) > int(permutations[a][b]):
                    count += 1
        list1.append(int(count))
    return list1


def det(m, permutations, inversion):
    '''
    Рахує визначник матриці m,
    використовуючи списки перестановок і інверсій
    '''
    r = 0
    for i in range(0, factorial(len(m))):
        b = 1
        for a in range(0, len(m)):
            b *= m[a, int(permutations[i][a]) - 1]
        r += ((-1) ** (inversion[i])) * b
    return r


while True:
    while True:
        print("")
        dim = input("x = ")
        if dim == "":
            print("\n"*6, "Бувайте здорові!", "\n"*5)
            break
        try:
            dim = int(dim)
            if 9 >= dim >= 1:
                break
            else:
                print("Це число не можна вводити!")
        except ValueError:
            print("Це не число!")
    if dim == "":
        break
    matrix = random_matrix(dim)
    result = det(matrix, f_permutations(dim), f_inversion(dim, f_permutations(dim)))
    print_matrix(matrix)
    print("det(matrix) = ", result, " ( Похибка : ", math.fabs(int(np.linalg.det(matrix)) - result), " )", sep="")
