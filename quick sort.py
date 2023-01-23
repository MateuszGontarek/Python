def pivotFunc(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if sum(arr[j]) < sum(pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pivot = pivotFunc(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
    return arr

tab = list(map(int, input().split()))
arrOfArrays = []
for i in range(tab[0]):
    arr = list(map(float, input().split()))

    arrOfArrays.append(arr)
low = 0
high = len(arrOfArrays) - 1
arrOfArrays = quickSort(arrOfArrays, low, high)
arrOfArrays.reverse()
for i in range(tab[2]):
    for j in range(len(arrOfArrays[i])):
        print(arrOfArrays[i][j], end="")
        if not j == tab[1] - 1:
            print(" ", end="")

    print()


