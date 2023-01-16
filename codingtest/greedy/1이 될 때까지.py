n, k = map(int, input().split())

result = 0

while True:
    if n % k == 0:
        result += n//k
        break
    n -= 1
    result += 1

print(result)

