def simulate():
    global curr_x, curr_y
    max_num = a[curr_x][curr_y]
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys) :
        next_x = curr_x + dx
        next_y = curr_y + dy
        if (inRange(next_x, next_y) and a[next_x][next_y] > max_num):
            max_num = a[next_x][next_y]
            curr_x = next_x
            curr_y = next_y
            return True
    return False

def inRange(x, y):
    if x in range(1, n + 1) and y in range(1, n + 1):
        return True
    else:
        return False

n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]
curr_x, curr_y = r,c

print(a[curr_x][curr_y], end= " ")
while   simulate():print(a[curr_x][curr_y], end=" ")