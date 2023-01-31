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
