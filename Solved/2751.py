from sys import stdin, stdout

def mergeSort(x):
    if len(x) > 1:
        middle = len(x)//2
        left = x[:middle]
        right = x[middle:]

        mergeSort(left)
        mergeSort(right)

        li, ri, i = 0, 0, 0
        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                x[i] = left[li]
                li += 1
            
            else:
                x[i] = right[ri]
                ri += 1
            
            i += 1
        
        x[i:] = left[li:] if li != len(left) else right[ri:]
    
    return x

a = int(stdin.readline())
b = []

for i in range(a):
    b.append(int(stdin.readline()))

mergeSort(b)

for i in range(len(b)):
    stdout.write(str(b[i]))
    stdout.write("\n")