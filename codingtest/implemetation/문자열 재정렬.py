s = input()

total_num = 0
words = []

for e in s:
    if e.isalpha():
        words.append(e)
    else:
        total_num += int(e)

words.sort()

if total_num != 0:
    words.append(str(total_num))

print(''.join(words))
