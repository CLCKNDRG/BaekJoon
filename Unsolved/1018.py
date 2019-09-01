n, m = input().split()
n = int(n)
m = int(m)
result = 64
swapTime = 0

table = []
refTable = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"]
]

for i in range(n):
    table.append(input())
    table[i] = list(table[i])

for i in range(n-8):
    for j in range(m-8):

        swapTime = 0
        for k in range(8):
            for l in range(8):
                if table[i+k][j+l] != refTable[k][l]:
                    swapTime+=1

        if swapTime > (64-swapTime):
            swapTime = 64-swapTime

        if swapTime < result:
            result = swapTime

print(result)