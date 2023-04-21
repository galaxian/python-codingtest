n = int(input())
cards_num = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))

dicts = {}

for num in cards_num:
    if num in dicts:
        dicts[num] += 1
    else:
        dicts[num] = 1

for num in find_num:
    if num in dicts:
        print(dicts[num], end=' ')
    else:
        print(0, end=' ')
