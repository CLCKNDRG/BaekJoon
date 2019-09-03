def insertionSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val

a = int(input())
b = []

for i in range (a):
    b.append(int(input()))

