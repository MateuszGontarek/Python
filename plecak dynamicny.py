def dynamic(products, weight):
    tab = [[0 for _ in range(weight + 1)] for _ in range(len(products) + 1)]
    
    for i in range(1, len(products) + 1):
        for j in range(1, weight + 1):
            if products[i - 1][1] <= j:
                tab[i][j] = max(products[i - 1][0] + tab[i - 1][j - products[i - 1][1]], tab[i - 1][j])
            else:
                tab[i][j] = tab[i - 1][j]
    return tab[-1][-1]

weight = int(input())
numberOfProducts = int(input())
products = []

for i in range(numberOfProducts):
    products.append(list(map(int, input().split())))

print(dynamic(products, weight))
