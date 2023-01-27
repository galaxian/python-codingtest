n = int(input())
fear = list(map(int, input().split(' ')))
fear.sort()

member = 0
party = 0

for elem in fear:
    member += 1
    if member >= elem:
        party += 1
        member = 0

print(party)
