S = str(input())

ans = 0
nums = list(S)

for num in nums:
    if ans + int(num) > ans * int(num):
        ans += int(num)
    else:
        ans *= int(num)

print(ans)
