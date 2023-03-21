n = int(input())

nums = str(n)
length = len(nums)

total = 0

for i in range(0, length//2):
    total += int(nums[i])

for i in range(length//2, length):
    total -= int(nums[i])

if total == 0:
    print('LUCKY')
else:
    print('READY')
