from collections import deque

def inRange(x, y):
    if x in range(0, n) and y in range(0, m):
        return True
    else:
        return False

def only_zero(grid):
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                return(False)
    return(True)

def bfs(x, y):
    queue = deque([(x,y)])
    global visited, a, count
    visited[x][y] = 2
    while queue:
        node = queue.popleft()
        curr_x, curr_y = node
        
        for i in range(4):
            move_x, move_y = curr_x + dxs[i], curr_y + dys[i]
            if (inRange(move_x, move_y)) and (visited[move_x][move_y]) == 0:
                visited[move_x][move_y] = 2
                queue.append((move_x,move_y))
            elif(inRange(move_x, move_y)) and (visited[move_x][move_y]) == 1:
                count += 1
                visited[move_x][move_y] = 3
                a[move_x][move_y] = 0


dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [row[:] for row in a]

t=0
count = 0
while not only_zero(a):
    count = 0
    bfs(0,0)
    t += 1
    if only_zero(a):
        break
    a = [row[1:m-1] for row in a[1:n-1]]
    visited = [row[:] for row in a]
    n -= 2
    m -= 2
print("%d %d" %(t, count))