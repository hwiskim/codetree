from collections import deque

def inRange(x, y):
    if x in range(0, n) and y in range(0, n):
        return True
    else:
        return False
    
def bfs(x, y):
    global copy
    queue = deque([(x,y)])
    curr_value = a[x][y]
    temp = [[0 for _ in range(n)] for _ in range(n)]
    temp[x][y] = curr_value
    copy[x][y] = 0
    while queue:
        node = queue.popleft()
        curr_x, curr_y = node
        copy[curr_x][curr_y] = 0
        for i in range(4):
            move_x, move_y = curr_x + dxs[i], curr_y + dys[i]
            if (inRange(move_x, move_y)) and copy[move_x][move_y] == curr_value:
                copy[move_x][move_y] = 0
                temp[move_x][move_y] = curr_value
                queue.append((move_x,move_y))
    return temp

def make_map():
    art_map= []
    for x in range(n):
        for y in range(n):
            if(copy[x][y] != 0):
                art_map.append(bfs(x,y))
    return art_map

def size_map(part):
    count = 0
    valueflag = 0
    for x in range(n):
        for y in range(n):
            if(part[x][y] != 0):
                if not valueflag:
                    valueflag = part[x][y]
                count += 1
    return (count,valueflag)

def comb_bfs(x,y,grid):
    queue = deque([(x,y)])
    value = grid[x][y]
    count = 0
    grid[x][y] = 0
    while queue:
        node = queue.popleft()
        curr_x, curr_y = node
        for i in range(4):
            move_x, move_y = curr_x + dxs[i], curr_y + dys[i]
            if not inRange(move_x, move_y) or grid[move_x][move_y] == 0:
                continue
            if (grid[move_x][move_y]) == value:
                grid[move_x][move_y] = 0
                queue.append((move_x,move_y))
            else:
                count += 1
    return (count)

def find_first(grid):
    for x in range(n):
        for y in range(n):
            if grid[x][y] != 0:
                return(x,y)
    return(0,0)

def make_comb(grid1,grid2):
    result = [[grid1[i][j] + grid2[i][j] for j in range(len(grid1[0]))] for i in range(len(grid1))]
    x,y = find_first(result)
    touch = comb_bfs(x,y,result)
    return touch


dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


copy = [row[:] for row in a]
art_map = make_map()
value_size = []
for i in range(len(art_map)):
    value_size.append(size_map(art_map[i]))

pos_com = []
for i in range(len(art_map)):
    for j in range(i+1,len(art_map)):
        touch = make_comb(art_map[i],art_map[j])
        if touch:
            pos_com.append((i,j,touch))
total = 0
for pos in pos_com:
    size = value_size[pos[0]][0] + value_size[pos[1]][0]
    value1 = value_size[pos[0]][1]
    value2 = value_size[pos[1]][1]
    total += size*value1*value2*pos[2]


print(total)
