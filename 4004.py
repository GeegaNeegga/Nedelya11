n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

color = [0] * n  # 0 - white, 1 - gray, 2 - black
has_cycle = False

def dfs(v):
    global has_cycle
    color[v] = 1  # серый
    for u in range(n):
        if graph[v][u]:
            if color[u] == 0:
                dfs(u)
            elif color[u] == 1:
                has_cycle = True
    color[v] = 2  # черный

for i in range(n):
    if color[i] == 0:
        dfs(i)

print(1 if has_cycle else 0)
