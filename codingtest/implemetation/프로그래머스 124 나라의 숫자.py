def solution(n):
    rev_base = ''
    table = {'1':'1', '2':'2', '0':'4'}
    while n > 0:
        n, mod = divmod(n, 3)
        if mod == 0:
            n = n - 1
        rev_base += table[str(mod)]
    return rev_base[::-1]


for i in range(1, 5):
    print(solution(i))
