from string import ascii_lowercase

s = str(input())
alphabet_list = list(ascii_lowercase)

for alphabet in alphabet_list:
    print(s.find(alphabet), end=' ')
