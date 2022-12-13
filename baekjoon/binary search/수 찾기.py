N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

A.sort()

for i in range(M):

    min = 0
    max = N - 1
    mid = (min + max) // 2

    target = arr[i]

    while min <= max:
        if A[mid] == target:
            print(1)
            break
        if A[mid] < target:
            min = mid + 1
        else:
            max = mid - 1
        mid = (min + max) // 2
    if min > max:
        print(0)
