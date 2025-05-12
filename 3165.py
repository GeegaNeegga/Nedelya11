from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().split()

index = 0
case_number = 1

while True:
    n = int(data[index])
    index += 1
    if n == 0:
        break

    l = int(data[index])
    index += 1

    graph = defaultdict(list)
    for _ in range(l):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2

    color = [-1] * (n + 1)
    is_bipartite = True
    queue = deque()

    # Стартуем с вершины 1 (по условию граф связный)
    queue.append(1)
    color[1] = 0

    while queue and is_bipartite:
        u = queue.popleft()
        for v in graph[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                is_bipartite = False
                break

    print(f"Test {case_number}: {'YES' if is_bipartite else 'NO'}")
    case_number += 1
