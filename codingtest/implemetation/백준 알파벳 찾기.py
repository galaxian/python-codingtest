from string import ascii_lowercase

s = str(input())
alphabet_list = list(ascii_lowercase)

result = []

for alphabet in alphabet_list:
    result.append(str(s.find(alphabet)))

print(' '.join(result))
