import string
import random


def stroka_1(num):
    stroka = ''
    for i in range(num):
        stroka += random.choice(string.ascii_letters)
    return stroka


print(stroka_1(12))


def stroka_2(stroka):
    s = list(stroka)
    big = 0
    small = 0
    for sym in s:
        if sym.isupper():
            big += 1
        else:
            small += 1
        if big > small:
            return 1
        elif small > big:
            return 0
        else:
            return -1


print(stroka_2(stroka_1(4)))


def stroka_3(length, num):
    list_ = []
    for i in range(num):
        list_.append(stroka_1(length))
    return list_


print(stroka_3(4, 3))


def stroka_4(argument):
    a = argument
    upper = []
    lower = []
    middle = []
    for i in a:
        s = list(i)
        big = 0
        small = 0
        for sym in s:
            if sym.isupper():
                big += 1
            else:
                small += 1
            if big > small:
                upper.append(i)
            elif small > big:
                lower.append(i)
            else:
                middle.append(i)
    up_num = (len(upper) / len(a)) * 100
    low_num = (len(lower) / len(a)) * 100
    mid_num = (len(middle) / len(a)) * 100
    print(up_num)
    print(low_num)
    print(mid_num)


stroka_4(stroka_3(5, 10))