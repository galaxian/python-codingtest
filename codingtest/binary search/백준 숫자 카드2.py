n = int(input())
cards_num = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))

cards_num.sort()
result = []


def lower_bound(arr, target):
    cur_min = 0
    cur_max = len(arr)

    while cur_min < cur_max:
        mid = (cur_min + cur_max) // 2
        if target <= arr[mid]:
            cur_max = mid
        else:
            cur_min = mid + 1

    return cur_min


def upper_bound(arr, target):
    cur_min = 0
    cur_max = len(arr)

    while cur_min < cur_max:
        mid = (cur_min + cur_max) // 2
        if target < arr[mid]:
            cur_max = mid
        else:
            cur_min = mid + 1

    return cur_min


for i in range(m):
    result.append(upper_bound(cards_num, find_num[i]) - lower_bound(cards_num, find_num[i]))

print(*result)
