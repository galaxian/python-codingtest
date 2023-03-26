n = int(input())
k = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
rotate = []

for _ in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    rotate.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 1, 1
arr[x][y] = 2
direction = 0
time = 0
idx = 0
q = [(x, y)]
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1 <= nx <= n and 1 <= ny <= n and arr[nx][ny] != 2:
        if arr[nx][ny] == 0:
            arr[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            arr[px][py] = 0
        if arr[nx][ny] == 1:
            arr[nx][ny] = 2
            q.append((nx, ny))
    else:
        time += 1
        break
    x, y = nx, ny
    time += 1
    if idx < l and time == rotate[idx][0]:
        if rotate[idx][1] == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        idx += 1

print(time)
