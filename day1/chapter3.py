def inRange(x, y):
    if x in range(0, n) and y in range(0, n):
        return True
    else:
        return False

def simulate(curr_x, curr_y):
    max_num = 0
    max_x = max_y = -1
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        next_x = curr_x + dx
        next_y = curr_y + dy
        if (inRange(next_x, next_y) and a[next_x][next_y] > max_num):
            max_num = a[next_x][next_y]
            max_x = next_x
            max_y = next_y
    curr_x = max_x
    curr_y = max_y
    return (curr_x, curr_y)

def grid_check():
    grid = [[0] * n for _ in range(n)]
    global r,c
    poplist = []
    for i in range(len(r)):
        grid[r[i]][c[i]] += 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 1:
                for k in range(len(r)):
                    if r[k] == i and c[k] == j:
                        poplist.append(k)
    poplist.sort()
    poplist.reverse()
    for popnum in poplist:
        r.pop(popnum)
        c.pop(popnum)

#def area

n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] - 1 for pos in marbles]
c = [pos[1] - 1 for pos in marbles]


# Please write your code here.
for _ in range(t):
    for i in range(len(r)):
        temp_x, temp_y = r[i], c[i]
        r[i], c[i] = simulate(temp_x, temp_y)
    grid_check()
print(len(r))
