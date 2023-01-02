n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0

while start <= end:
    wood = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            wood += i - mid
    if wood < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
