def is_bipartite(n, graph):
    color = [-1] * (n + 1)  # 1-based индексация

    def dfs(v, c):
        color[v] = c
        for u in graph[v]:
            if color[u] == -1:
                if not dfs(u, 1 - c):
                    return False
            elif color[u] == color[v]:
                return False
        return True

    for i in range(1, n + 1):
        if color[i] == -1:
            if not dfs(i, 0):
                return False
    return True

# Ввод
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Проверка и вывод
print("YES" if is_bipartite(n, graph) else "NO")
