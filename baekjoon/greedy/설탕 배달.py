sugar = int(input())

answer = 0

while sugar >= 0:
    if sugar % 5 == 0:
        answer += sugar // 5
        print(answer)
        break
    sugar -= 3
    answer += 1
else:
    print(-1)
