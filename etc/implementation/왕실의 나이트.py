input_data = input()
r = int(input_data[1])
c = int(ord(input_data[0]) - int(ord('a'))) + 1

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0

for move in moves:
    next_r = r + move[0]
    next_c = c + move[1]
    if 8 > next_r > 0 and 8 > next_c > 0:
        result += 1

print(result)
