n, k = map(int, input().split())

cnt = 0

for h in range(n + 1):
    if h < 10:
        string_h = '0' + str(h)
    else:
        string_h = str(h)
    for m in range(60):
        if m < 10:
            string_m = '0' + str(m)
        else:
            string_m = str(m)
        for s in range(60):
            if s < 10:
                string_s = '0' + str(s)
            else:
                string_s = str(s)
            if str(k) in string_h + string_m + string_s:
                cnt += 1

print(cnt)
