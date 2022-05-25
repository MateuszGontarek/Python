import math
def merge_sort(arr):
    if len(arr) > 1:
        s = len(arr) // 2
        left = arr[:s]
        right = arr[s:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left,right)
    return arr[math.ceil(len(arr) * 0.1)::], math.ceil(len(arr) * 0.1)
def merge(lista,left, right):
    indexLeft = 0
    indexRight = 0
    index = 0
    while indexLeft < len(left) and indexRight < len(right):
        if left[indexLeft][2]   < right[indexRight][2]:
            lista[index] = left[indexLeft]
            indexLeft += 1
        else:
            lista[index] = right[indexRight]
            indexRight += 1
        index += 1
    while indexLeft < len(left):
        lista[index] = left[indexLeft]
        index += 1
        indexLeft += 1
    while indexRight < len(right):
        lista[index] = right[indexRight]
        index += 1
        indexRight += 1

x = int(input())
listaEndEnd = []

for i in range(x):
    lista = []
    row = input()
    while row != "-":
        row = row.split()
        listaTwo = []
        listaTwo.append(row[0])
        listaTwo.append(row[1])
        listaTwo.append(row[2])
        lista.append(listaTwo)
        row = input()
    ReturnValue = merge_sort(lista)
    lista = ReturnValue[0]
    lista = lista[::-1]
    lista = lista[0:ReturnValue[1]]
    listaEnd = []
    for i in range(len(lista)):
        listaEnd.append(lista[i][0])
        listaEnd.append(lista[i][1])
    listaEndEnd.append(listaEnd)

n = 0

for i in listaEndEnd:
    for j in i:
        if n % 2 == 0:
            print(j, end = " ")
            n = 1
        else:
            print(j)
            n = 0
    print("-")