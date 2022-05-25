def merge_sort(arr):
    if len(arr) > 1:
        s = len(arr) // 2
        left = arr[:s]
        right = arr[s:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left,right)
    return arr
def merge(lista,left, right):
    indexLeft = 0
    indexRight = 0
    index = 0
    while indexLeft < len(left) and indexRight < len(right):
        if left[indexLeft] < right[indexRight]:
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

lista = [2, 5, 1, 4, 8, 9, 0]

print(merge_sort(lista))