n = int(input())

nums = str(n)
length = len(nums)

left = 0
for i in range(0, length//2):
    left += int(nums[i])

right = 0
for i in range(length//2, length):
    right += int(nums[i])

if left == right:
    print('LUCKY')
else:
    print('READY')
