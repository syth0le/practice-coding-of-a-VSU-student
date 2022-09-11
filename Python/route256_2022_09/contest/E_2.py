class Field:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.up = None
        self.right = None
        self.down = None

    def __repr__(self):
        return self.value


def func(matrix, n, m):
    rows = n
    if rows == 0:
        return 0

    cols = m
    indegree = [[0 for x in range(cols)] for y in range(rows)]
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    for x in range(rows):
        for y in range(cols):
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                    if matrix[nx][ny] < matrix[x][y]:
                        indegree[x][y] += 1

    queue = []
    for x in range(rows):
        for y in range(cols):
            if indegree[x][y] == 0:
                queue.append((x, y))

    path_len = 0
    while queue:
        sz = len(queue)
        for i in range(sz):
            x, y = queue.pop(0)
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                    if matrix[nx][ny] > matrix[x][y]:
                        indegree[nx][ny] -= 1
                        if indegree[nx][ny] == 0:
                            queue.append((nx, ny))
        path_len += 1
    return path_len


t = int(input())
results = []
for i in range(t):
    n, m = list(map(int, input().split()))
    fields = []
    for i in range(n):
        temp = list(input())
        fields.append(temp)
    print(fields)
    answer = func(fields, n, m)
    results.append(answer)

for i in results:
    print(i)
