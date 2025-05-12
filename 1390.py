import sys
sys.setrecursionlimit(200000)

n, m = map(int, input().split())
edges_set = set()
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    if u != v:
        edge = tuple(sorted((u, v)))
        if edge not in edges_set:
            edges_set.add(edge)
            graph[u].append(v)
            graph[v].append(u)

visited = [False] * (n + 1)
has_cycle = False

def dfs(v, parent):
    global has_cycle
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, v)
        elif u != parent:
            has_cycle = True

dfs(1, -1)

print("YES" if has_cycle else "NO")
