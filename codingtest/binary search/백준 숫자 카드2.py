from bisect import bisect_left,bisect_right

n = int(input())
cards_num = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))

cards_num.sort()
result = []

for i in range(m):
    result.append(bisect_right(cards_num, find_num[i]) - bisect_left(cards_num, find_num[i]))

print(*result)
