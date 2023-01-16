n = int(input())

arr = []
for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key=lambda score: score[1])

for e in arr:
    print(e[0], end=' ')