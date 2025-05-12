from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
in_degree = defaultdict(int)
names = set()

for _ in range(n):
    relation = input().strip()
    if "<" in relation:
        a, b = relation.split("<")
        graph[a].append(b)
        in_degree[b] += 1
        names.update([a, b])
    else:
        a, b = relation.split(">")
        graph[b].append(a)
        in_degree[a] += 1
        names.update([a, b])

# Все гномы должны быть в словарях
for name in names:
    if name not in in_degree:
        in_degree[name] = 0

# Топологическая сортировка (Kahn's Algorithm)
q = deque()
for node in names:
    if in_degree[node] == 0:
        q.append(node)

count = 0
while q:
    u = q.popleft()
    count += 1
    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            q.append(v)

print("possible" if count == len(names) else "impossible")
