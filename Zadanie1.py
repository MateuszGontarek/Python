def f(lista):
    lista = sorted(lista, key=lambda x: x[2])
    listunia = [lista[0]]

    hour = listunia[0][1]
    for i in range(1, len(lista)):
        if hour <= lista[i][1]:
            listunia.append(lista[i])
            hour = lista[i][2]
    return listunia

lista = [['Z1',11,12],['Z2',8,9],['Z3',10,11],['Z4',10,13],['Z5',13,14],['Z6',12,15],['Z7',15,16]]

print(f(lista))