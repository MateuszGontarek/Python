def dynamic(n, change):
    tab = [i + 1 for i in range(change)]

    for i in range(1, len(n)):
        for j in range(change):
            if n[i] == j + 1:
                tab[j] = 1
            elif j  - n[i] >= 0:
                tab[j] = tab[j - n[i]] + 1
    return tab

print(dynamic([1, 3, 5], 20))




