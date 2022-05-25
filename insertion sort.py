lista = list(map(int,input().split()))
for i in range(1, len(lista)):
    indeks = i - 1
    number = lista[i]
    while number < lista[indeks] and not indeks < 0:
        lista[indeks + 1] = lista[indeks]
        indeks -= 1
    lista[indeks + 1] = number
print(lista)
        
