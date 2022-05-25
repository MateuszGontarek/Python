lista = list(map(float, input().split()))
number = int(input())
def kubelkowe(number, lista):
    listaKubkow = []
    mini = min(lista)
    maks = max(lista)
    zakres = (maks - mini) / number
    for i in range(number):
        listunia = []
        listaKubkow.append(listunia)
    for i in lista:
        try:
            listaKubkow[int((i - mini) / zakres + mini)].append(i)
        except IndexError:
            listaKubkow[-1].append(i)
    for i in listaKubkow:
        i.sort()
        for j in i:
            print(j, end = ' ')
        print()
kubelkowe(number, lista)