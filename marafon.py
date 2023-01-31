def bank(a, years):
    for i in range(years):
        a = a + a * 0.1
    return a
