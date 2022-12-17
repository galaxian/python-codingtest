n, m = map(int, input().split())

result = 0

for i in range(n):
    numbers = list(map(int, input().split()))
    min_number = min(numbers)
    result = max(result, min_number)

print(result)
