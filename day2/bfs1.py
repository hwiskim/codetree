from collections import deque

def inRange(x, y):
    if x in range(0, n) and y in range(0, m):
        return True
    else:
        return False

def bfs(x, y):
    queue = deque([(x,y)])
    global visited
    visited[x][y] = 0
    
    while queue:
        node = queue.popleft()
        if node == (n - 1, m - 1):
            return 1
        curr_x, curr_y = node
        for i in range(4):
            move_x, move_y = curr_x + dxs[i], curr_y + dys[i]
            if not inRange(move_x, move_y):
                continue
            if (inRange(move_x, move_y)) and (visited[move_x][move_y]):
                visited[move_x][move_y] = 0
                queue.append((move_x,move_y))
    return 0

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = a
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

print(bfs(0,0))