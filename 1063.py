# Напишем решение с использованием DFS для поиска связных компонент.

def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                stack.append((nx, ny))

m, n = map(int, input().split())
grid = [input().strip() for _ in range(m)]
visited = [[False] * n for _ in range(m)]

count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '#' and not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)
