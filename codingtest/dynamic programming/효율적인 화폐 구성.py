n, m = map(int, input().split(' '))

money = []
MAX_INT = 10001

for i in range(n):
    money.append(int(input()))

dp = [MAX_INT] * (m + 1)

dp[0] = 0

for i in range(1, n):
    for j in range(money[i], m + 1):
        if dp[j - money[i]] != MAX_INT:
            dp[j] = min(dp[j], dp[j - money[i]] + 1)

if dp[m] == MAX_INT:
    print(-1)
else:
    print(dp[m])
