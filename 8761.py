n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = int(input())

# Сортируем списки смежности для устойчивого порядка обхода
for neighbors in graph:
    neighbors.sort()

visited = [False] * (n + 1)
d = [0] * (n + 1)
f = [0] * (n + 1)
time = 1

def dfs(v):
    global time
    visited[v] = True
    d[v] = time
    time += 1
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
    f[v] = time
    time += 1

dfs(start)

for i in range(1, n + 1):
    print(d[i], f[i])

