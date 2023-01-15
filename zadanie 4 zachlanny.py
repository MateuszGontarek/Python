def make_better_tab(tab):
    tab2 = []
    for i in tab: 
        for j in i:
            tab2.append(j)
    return tab2
def f(payload, tab):
    tab = sorted(make_better_tab([[[i[1] , i[0]] for j in range(i[2])] for i in tab]), key=lambda x: x[0] / x[1], reverse=True)
    value = 0

    for i in tab:
        if payload - i[1] >= 0:
            payload -= i[1]
            value += i[0]
        if payload == 0: break
    return value

print(f(20, [[5, 10, 2],[10,5, 5],[10,10, 1],[2,4, 2],[4,2, 3],[5,5, 1]]))