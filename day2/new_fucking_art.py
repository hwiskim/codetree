#깔끔하게 풀어보자

from collections import deque

def in_range(x,y):
    return 0 <= x and x < num and \
            0 <= y and y < num



#make_group 함수들
def make_group(x,y):

    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]

    global group_index

    group_key = ["g_num", "g_size"]
    group_value = []
    #키 순서대로 넣도록 조심
    index = group_index
    group_num = art[x][y]
    size = 1
    #bfs 시작, 상하좌우 돌며서 재귀 시작
    g_q = deque([(x,y)])
    pos_group = deque()
    visited[x][y] = index

    #bfs돌면서 visited 채우기
    while g_q:
        cur_x,cur_y = g_q.popleft()

        for dx,dy in zip(dxs,dys):
            new_x, new_y = cur_x + dx, cur_y + dy

            if not in_range(new_x,new_y) or visited[new_x][new_y]:
                continue
            if art[new_x][new_y] == group_num:
                g_q.append((new_x,new_y))
                visited[new_x][new_y] = index
                size += 1
            if art[new_x][new_y] != group_num:
                pos_group.append((new_x,new_y))
    #재귀시작
    for new_x, new_y in pos_group:
        if not visited[new_x][new_y]:
            group_index += 1
            make_group(new_x, new_y)
    #조합 만들기
    while pos_group:
        cur_x,cur_y = pos_group.popleft()
        edge_coount = 1
        cur_group = visited[cur_x][cur_y]
        repeat_count = len(pos_group)
        for _ in range(repeat_count):
            new_x,new_y = pos_group.popleft()
            if visited[new_x][new_y] == cur_group:
                edge_coount += 1
            else:
                pos_group.append((new_x,new_y))
        combine.append((index, cur_group, edge_coount))
    #group 값을 순서대로 채우기, 딕셔너리 만들기
    group_value.append(art[x][y])
    group_value.append(size)
    value = dict(zip(group_key,group_value))
    groups[index] = value

#계산기 함수
def calculate_art_point():
    total = 0
    while combine:
        group_a, group_b, edge_num = combine.popleft()
        total_size = groups[group_a]['g_size'] + groups[group_b]['g_size']
        a_num = groups[group_a]['g_num']
        b_num = groups[group_b]['g_num']
        total += total_size * a_num * b_num * edge_num
    return total

#비기 풍차 돌리기 함수 1차 상
def change_grid_1():
    mid = num // 2
    for i in range(mid):
        w_x = [i, mid, num - 1 - i, mid]
        w_y = [mid, num - 1 - i, mid, i]
        for j in range(3):
            x,y = w_x[j],w_y[j]
            n_x,n_y = w_x[j + 1],w_y[j + 1]
            art[x][y], art[n_x][n_y] = art[n_x][n_y], art[x][y]

def change_grid_2():
    mid = num // 2
    start = mid + 1
    end = mid - 1
    s_x = [0, 0, start, start]
    s_y = [0, start, 0, start]
    for i in range(4):
        x,y = s_x[i],s_y[i]
        copy = [row[y:y+mid] for row in art[x:x+mid]]
        for j in range(mid):
            for k in range(mid):
                art[x+j][y+k] = copy[end-k][j]

#예술점수를 구하기 위한 여정...시작
num = int(input())
art = [list(map(int, input().split())) for _ in range(num)]
art_point = 0

for i in range(4):
    if i != 0:
        change_grid_1()
        change_grid_2()
    #0장 그룹을 나누기 위한 가본곳 채크
    visited = [[0 for _ in range(num)] for _ in range(num)]
    #1장 아트보고 그룹 나누기, 그룹 인자 채우기, 조합 만들기
    groups = {}
    group_index = 1
    combine = deque() #조합, (그룹 a, 그룹 b, 접합변 수)
    make_group(0,0)
    #2장 만든 딕셔너리 참고해서 예술 점수 구하기
    art_point += calculate_art_point()

print(art_point)
