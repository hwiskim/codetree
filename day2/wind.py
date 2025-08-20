dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def inRange(x, y):
    if x in range(0, n) and y in range(0, m):
        return True
    else:
        return False

def container():
    global a
    curr_x, curr_y = (f_x, f_y)
    len = ((l_x - f_x) + (l_y - f_y)) * 2
    change_d = [l_x - f_x,l_y - f_y, l_x - f_x,l_y - f_y]
    i = 0
    for _ in range(len - 1):
        if not change_d[i]:
            i += 1
        next_x, next_y = curr_x + dxs[i], curr_y + dys[i]
        a[curr_x][curr_y], a[next_x][next_y] = a[next_x][next_y], a[curr_x][curr_y]
        curr_x, curr_y = next_x, next_y
        change_d[i] -= 1

def average(x, y):
    curr_x, curr_y = (x, y)
    curr_val= a[curr_x][curr_y]
    count = 1
    for i in range(4):
        next_x, next_y = curr_x + dxs[i], curr_y + dys[i]
        if inRange(next_x, next_y):
            curr_val += a[next_x][next_y]
            count += 1
    return(curr_val // count)

n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]



for i in range(q):
    f_x, f_y, l_x, l_y = (x-1 for x in winds[i])
    container()
    copy = [row[:] for row in a]
    for x in range(f_x, l_x + 1):
        for y in range(f_y, l_y + 1):
            copy[x][y] = average(x,y)
    for x in range(f_x, l_x + 1):
        for y in range(f_y, l_y + 1):
            a[x][y] = copy[x][y]
for row in a:
    print(*row)