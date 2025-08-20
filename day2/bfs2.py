from collections import deque

def inRange(x, y):
    if x in range(0, n) and y in range(0, n):
        return True
    else:
        return False

def bfs(x, y):
    queue = deque([(x,y)])
    global visited, count
    if visited[x][y] == 0:
        visited[x][y] = 1
        count += 1
    while queue:
        node = queue.popleft()
        curr_x, curr_y = node
        for i in range(4):
            move_x, move_y = curr_x + dxs[i], curr_y + dys[i]
            if (inRange(move_x, move_y)) and (visited[move_x][move_y]) == 0:
                visited[move_x][move_y] = 1
                queue.append((move_x,move_y))
                count += 1

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = a

points = [tuple(map(int, input().split())) for _ in range(k)]
r = [pos[0] - 1 for pos in points]
c = [pos[1] - 1 for pos in points]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
count = 0
for i in range(k):
    bfs(r[i], c[i])
print(count)