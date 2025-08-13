def inRange(x, y):
    if x in range(1, n+1) and y in range(1, n+1):
        return True
    else:
        return False
#격자에 있는지

def canMove(runner_x, runner_y):
    if abs(curr_x - runner_x) + abs(curr_y - runner_y) <= 3:
        return True
    else:
        return False
#움직일수있는지

#러너야 움직여야한다
def runnerMove():
    for i in range(m):
        if not inRange(r_r[i] + dxs[r_d[i]], r_c[i] + dys[r_d[i]]):
            r_d[i] = (r_d[i] + 2) % 4
        if canMove(r_r[i], r_c[i]) and (curr_x, curr_y) != (r_r[i] + dxs[r_d[i]], r_c[i] + dys[r_d[i]]):
            r_r[i] = r_r[i] + dxs[r_d[i]]
            r_c[i] = r_c[i] + dys[r_d[i]]


def runnerOut(catch_x, catch_y):
    poplist = []
    global r_r,r_c,r_d,m
    for i in range(m):
        if catch_x == r_r[i] and catch_y == r_c[i] and not t_grid[catch_x][catch_y]:
            poplist.append(i)
    point = len(poplist)
    m -= point
    poplist.reverse()
    for popnum in poplist:
        r_r.pop(popnum)
        r_c.pop(popnum)
        r_d.pop(popnum)
    return(point)
#술래 돌게 만들기

#상우하좌
# qkdgid = ["↑","→","↓","←"]
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

n, m, h, k = map(int, input().split())
#인자 받기


runner = [tuple(map(int, input().split())) for _ in range(m)]
r_r = [pos[0] for pos in runner]
r_c = [pos[1] for pos in runner]
r_d = [pos[2] for pos in runner]


#트리 위치
tree = [tuple(map(int, input().split())) for _ in range(h)]
t_r = [pos[0] for pos in tree]
t_c = [pos[1] for pos in tree]

t_grid = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(h):
    t_grid[t_r[i]][t_c[i]] += 1


count = 0
even = 2
handle = 0
start_place = (n//2 + 1, n//2 + 1)
curr_x, curr_y = start_place
move_line = []
look_way = []
move_line.append(start_place)
look_way.append(handle)

#풍차 구문부터 리펙
for _ in range(1, n ** 2 - 1):
    curr_x, curr_y = (curr_x + dxs[handle % 4], curr_y + dys[handle % 4])
    move_line.append((curr_x, curr_y))
    count+=1
    if count == even // 2:
        handle+=1
    elif count == even:
        even += 2
        count = 0
        handle+=1
    look_way.append(handle % 4)
move_line.append((1, 1))

count = 0
score = 0
#디버깅용
# temp = 0
# visual = [[0] * (n + 1) for _ in range(n + 1)]
# visual[n//2 + 1][n//2 + 1] = 1
for turn in range(1, k+1):
    curr_x, curr_y = move_line[count]
    count += 1
    if count % (n**2 - 1) == 0:
        move_line.reverse()
        for i in range(0, len(look_way)):
            look_way[i] = (look_way[i] + 2) % 4 
        look_way.reverse()
        count = 0
    runnerMove()
    curr_x, curr_y = move_line[count]
    look = look_way[count]
    # visual[curr_x][curr_y] += 1
    for i in range(3):
        score += turn * runnerOut(curr_x + dxs[look]*i, curr_y + dys[look]*i)
#디버깅 존
    # if temp != score:
    #     print("현재 %d턴!! %d득점! 누적점수는 %d!!" %(turn, score - temp, score))
    #     temp = score
print(score)