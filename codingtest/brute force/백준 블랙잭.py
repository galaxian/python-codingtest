from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0

# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             temp = cards[i] + cards[j] + cards[k]
#             if temp > m:
#                 continue
#             else:
#                 result = max(result, temp)

for cards in combinations(cards, 3):
    temp = sum(cards)
    if result < temp <= m:
        result = temp

print(result)
