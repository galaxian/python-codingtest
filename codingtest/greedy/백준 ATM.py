n = int(input())
people = list(map(int, input().split()))

people.sort()
result = 0

for i in range(n):
    result += people[i] * (n - i)

print(result)
