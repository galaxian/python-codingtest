n, m = map(int, input().split())
balls = list(map(int, input().split()))

arr = [0] * 11

for e in balls:
    arr[e] += 1

ans = 0

for i in range(1, m + 1):
    n -= arr[i]
    ans += arr[i]*n

print(ans)
