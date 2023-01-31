def bank(a, years):
    for i in range(years):
        a = a + a * 0.1
    return a


def palindrome(str1):
    if str1 == str1[::-1]:
        return True
    return False
