S = str(input())

ans = 0
nums = list(S)

for num in nums:
    ans = max(ans + int(num), ans * int(num))

print(ans)
