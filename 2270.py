import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

color = [0] * (n + 1)
parent = [0] * (n + 1)
cycle = []

def dfs(v):
    global cycle
    color[v] = 1  # серый
    for u in graph[v]:
        if color[u] == 0:
            parent[u] = v
            if dfs(u):
                return True
        elif color[u] == 1:
            # Найден цикл
            cycle = []
            cur = v
            while cur != u:
                cycle.append(cur)
                cur = parent[cur]
            cycle.append(u)
            cycle.append(v)
            cycle.reverse()
            return True
    color[v] = 2  # черный
    return False

for v in range(1, n + 1):
    if color[v] == 0:
        if dfs(v):
            print("YES")
            print(*cycle)
            break
else:
    print("NO")
