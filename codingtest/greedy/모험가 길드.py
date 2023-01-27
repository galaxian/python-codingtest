n = int(input())
fear = list(map(int, input().split(' ')))
fear.sort(reverse=True)

result = 0

while fear:
    if len(fear) < fear[0]:
        break
    fear = fear[fear[0]:]
    result += 1

print(result)
