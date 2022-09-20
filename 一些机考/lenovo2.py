m, n, x, y = 2, 2, 1, 1


def dfs(visited, m, n, que):
    new_que = []
    for qx, qy in que:
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = qx + di
            new_y = qy + dj
            if new_x < 0 or new_y < 0 or new_x > m - 1 or new_y > n - 1 or visited[new_x][new_y] == 1:
                continue
            else:
                visited[new_x][new_y] = 1
                new_que.append((new_x, new_y))
    return new_que


visited = [[0 for _ in range(n)] for _ in range(m)]
visited[x-1][y-1] = 1
que = [(x-1, y-1)]
count = 0
for step in range(1000):
    que = dfs(visited, m, n, que)
    count = max(count, len(que))
    if len(que) == 0:
        break
print(count)


