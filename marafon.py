import math


def bank(a, years):
    for i in range(years):
        a = a + a * 0.1
    return a


def palindrome(str1):
    if str1 == str1[::-1]:
        return True
    return False


def is_prime(number):
    if number == 1:
        return True
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i = i + 1
    return True


def square(a):
    t = (4*a, a*a, math.sqrt(2*a*a))
    return t


def is_year_leap(year):
    if year % 4 == 0:
        return True
    return False


def common(str1, str2):
    l = []
    for i in str1:
        if str2.count(i) > 0 and i not in l:
            l.append(i)
    return l


def characters_1(str1):
    str1 = str1.lower()
    m = {}
    for i in str1:
        m[i] = str1.count(i)
    return m


def razb(l):
    if len(l) % 3 == 0:
        s1 = s2 = len(l) // 3
    elif len(l) % 3 == 1:
        s1 = s2 = len(l) // 3
    else:
        s1 = len(l) // 3
        s2 = len(l) // 3 + 1
    l1 = l[:s1]
    l2 = l[s1:s1+s2]
    l3 = l[s1+s2:]
    return l1[::-1], l2[::-1], l3[::-1]
