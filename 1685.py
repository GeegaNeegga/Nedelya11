import math

# Функция для выполнения поиска в глубину
def dfs(x, y, visited, stations, n):
    stack = [(x, y)]
    visited[x][y] = True
    while stack:
        cx, cy = stack.pop()
        for i in range(n):
            if not visited[i]:
                dist = (stations[cx][0] - stations[i][0])**2 + (stations[cx][1] - stations[i][1])**2
                if dist < 4:
                    visited[i] = True
                    stack.append(i)

n = int(input())  # количество станций
stations = [tuple(map(int, input().split())) for _ in range(n)]  # координаты станций
visited = [False] * n  # список посещенных станций

count = 0
# Проходим по всем станциям
for i in range(n):
    if not visited[i]:  # если станция еще не посещена, значит, это новая земля
        dfs(i, i, visited, stations, n)  # выполняем DFS для поиска всех связанных станций
        count += 1  # увеличиваем количество земель

print(count)
