from collections import deque

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '0':
                visited[nx][ny] = True
                queue.append((nx, ny))

count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '0' and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
