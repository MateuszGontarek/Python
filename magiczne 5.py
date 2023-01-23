k = int(input())
n = int(input())
array = []
for i in range(n):
    row = input().split()
    array.append([row[0], int(row[1])])

def f(array, k):
    if len(array) > 5:
        arrayOfArrays = []
        tab = []

        for i in range(len(array)):
            tab.append(array[i])
            if len(tab) == 5:
                arrayOfArrays.append(sorted(tab, key=lambda x: x[1]))
                tab = []
        if len(tab) > 0:
            arrayOfArrays.append(sorted(tab, key=lambda x: x[1]))
            
        arrayOfMedians = [i[len(i) // 2][1] for i in arrayOfArrays]
        median = arrayOfMedians[len(arrayOfMedians) // 2]
        arrayBigger = []
        for i in array:
            if i[1] >= median: 
                arrayBigger.append(i)
        f(arrayBigger, (len(array) - len(arrayBigger)))
    else:
        array = sorted(array, key=lambda x: x[1])[-1]
        print(array[0])
        print(array[1])
f(array, k)