# Напишем функцию для поиска в глубину (DFS)
def dfs(x, y, n, maze, visited):
    # Проверяем, что клетка в пределах лабиринта и является пустой
    if x < 0 or x >= n or y < 0 or y >= n or maze[x][y] == '*' or visited[x][y]:
        return 0
    # Помечаем клетку как посещенную
    visited[x][y] = True
    # Считаем данную клетку
    area = 1
    # Пытаемся пройти в соседние клетки
    area += dfs(x + 1, y, n, maze, visited)  # вниз
    area += dfs(x - 1, y, n, maze, visited)  # вверх
    area += dfs(x, y + 1, n, maze, visited)  # вправо
    area += dfs(x, y - 1, n, maze, visited)  # влево
    return area

# Ввод данных
n = int(input())  # размер лабиринта
maze = [list(input().strip()) for _ in range(n)]  # лабиринт
x, y = map(int, input().split())  # координаты клетки, с которой начинается поиск

# Преобразуем координаты из 1-индексации в 0-индексацию
x -= 1
y -= 1

# Массив посещенных клеток
visited = [[False] * n for _ in range(n)]

# Ищем площадь комнаты с помощью DFS
area = dfs(x, y, n, maze, visited)

# Выводим результат
print(area)
