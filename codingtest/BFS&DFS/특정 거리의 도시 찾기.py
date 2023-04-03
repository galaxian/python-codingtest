from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (n + 1)
visited[x] = 0

queue = deque([x])
while queue:
    pop = queue.popleft()
    for i in graph[pop]:
        if visited[i] == -1:
            visited[i] = visited[pop] + 1
            queue.append(i)

ck = False
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        ck = True

if not ck:
    print(-1)
