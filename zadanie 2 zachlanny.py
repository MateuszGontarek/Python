def f(payload, tab):
    tab = sorted([[i[1] , i[0]] for i in tab], key=lambda x: x[0] / x[1])[::-1]
    value = 0
    for i in tab:
        if payload - i[1] >= 0:
            payload -= i[1]
            value += i[0]
    return value


tab = [[5, 10],[10,5],[10,10],[2,4],[4,2],[5,5]]
print(f(20, tab))