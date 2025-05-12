import sys

# Считываем все входные строки
lines = sys.stdin.read().splitlines()
n = int(lines[0])
edges = lines[1:]

# Инициализация графа
graph = [[] for _ in range(n + 1)]
for line in edges:
    if line.strip() == "":
        continue
    a, b = map(int, line.split())
    graph[a].append(b)
    graph[b].append(a)

# Сортировка смежных вершин для устойчивого порядка обхода
for neighbors in graph:
    neighbors.sort()

visited = [False] * (n + 1)
result = []
time = 1

def dfs(v):
    global time
    visited[v] = True
    gray = time
    time += 1
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
    black = time
    time += 1
    result.append((v, gray, black))

# Запускаем DFS для всех вершин по возрастанию
for v in range(1, n + 1):
    if not visited[v]:
        dfs(v)

# Выводим результат в порядке первого посещения
for v, gray, black in result:
    print(gray, black)
