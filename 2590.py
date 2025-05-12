from collections import deque
import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
grid = data[1:]

visited = [[False]*n for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '*':
                visited[nx][ny] = True
                queue.append((nx, ny))

asteroid_count = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == '*' and not visited[i][j]:
            bfs(i, j)
            asteroid_count += 1

print(asteroid_count)
