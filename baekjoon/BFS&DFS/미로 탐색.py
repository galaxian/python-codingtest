# N×M크기의 배열로 표현되는 미로가 있다.
#
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때
# 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
#
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.


# 최단 거리를 찾는 문제로 queue를 사용해
# 시작 지점에서 가까운 노드부터 차례대로 탐색하는 BFS를 사용해 해결했다.


from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # queue 구현을 위해 deque 사용
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        # 현재 위치에서 상,하,좌,우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 범위를 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 진행한 곳이 벽인 경우
            if graph[nx][ny] == 0:
                continue
            # 진행한 노드가 처음 방문하는 경우
            if graph[nx][ny] == 1:
                # 최단 거리 기록 및 큐에 추가
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
