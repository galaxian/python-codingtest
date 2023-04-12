n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
result = 0

for coin in coins:
    result += k // coin
    k = k % coin

print(result)
