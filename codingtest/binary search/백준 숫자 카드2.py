from collections import Counter

n = int(input())
cards_num = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))

cnt = Counter(cards_num)

for num in find_num:
    if num in cnt:
        print(cnt[num], end=' ')
    else:
        print(0, end=' ')
