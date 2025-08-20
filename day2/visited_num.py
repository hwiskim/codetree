from collections import deque

def in_range(x,y):
    return 0 <= x and x < num and \
            0 <= y and y < num


def can_go(x, y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def push(x,y):
    global order

    answer[x][y] = order
    order += 1
    visited[x][y] = 1
    q.append((x,y))

def bfs():
    dxs = [1,0]
    dys = [0,1]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                push(new_x, new_y)


num = int(input())
grid = [list(map(int, input().split())) for _ in range(num)]

q = deque()
order = 1
visited = [[0 for _ in range(num)] for _ in range(num)]
answer = [[0 for _ in range(num)] for _ in range(num)]
push(0,0)
bfs()
print("#"*10)
for a in answer:
    print(*a)

