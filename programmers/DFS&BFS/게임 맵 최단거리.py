def solution(maps):
    answer = -1
    # 방문 확인용 리스트 선언
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    # 시작점을 큐에 push하고 방문 리스트 체크
    queue = [(0, 0)]
    visited[0][0] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # BFS로 최단거리 탐색
    while queue:
        x, y = queue.pop(0)
        # x, y 좌표가 우하단 목적지일 경우 탈출
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return visited[x][y]
        # 상하좌우 모든 경우 고려
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return answer


# 결과값 11
map1 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(map1))

# 결과값 -1
map2 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(map2))
