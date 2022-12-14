M = int(input())

N = 1000 - M
cnt = 0
coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    cnt += N // coin
    N %= coin

print(cnt)
