'''
술래 : 정중앙에 위치

도망자 : 어딘가에 위치
- 도망자는 좌우 혹은 상하로 움직임

- 술래와의 거리가 3 이하인 도망자들만 움직일 수 있음
- > 거리 재는 함수
'''
# x1, y1 = 술래
# x2, y2 = 도망자

def distance(x1, y1, x2, y2):
    if (abs(x1-x2) + abs(y1-y2)) <= 3:
        return True
    else:
        return False

def move(x, y, direction):
    # cnt 는 바라보고 있는 방향

    if direction == 'up':
        x -= 1
    
    elif direction == 'down':
        x += 1

    elif direction == 'right':
        y += 1
    
    elif direction == 'left':
        y -= 1

    return x, y

def in_range(x, y, n):
    return 1<= x <= n and 1<= y <= n

# 술래 이동 구현
# n과, 몇 번째 이동인지만 정해지면 사실 정해져 있음
# u r /d d l l u u
# u r /d d l l /u u u r r r /d d d d l l l l /u u u u

def make_catcher_move_list(n):

    move_list = ['up', 'right', 'down', 'left']
    
    catcher_trace =[]

    m_idx = 0
    replay_count = 1
    two_count = 0

    while True:

        if two_count == 2:
            two_count = 0
            replay_count += 1

        for _ in range(replay_count):
            catcher_trace.append(move_list[m_idx])

        if len(catcher_trace) >= n*n :
            break

        m_idx += 1
        if m_idx == 4:
            m_idx -= 4
        two_count += 1

    return catcher_trace

def make_reversed_catcher_move_list(catcher_move_list):
    
    reversed_catcher_move_list = []

    for move in reversed(catcher_move_list):

        if move == 'up':
            reversed_catcher_move_list.append('down')
        
        elif move == 'down':
            reversed_catcher_move_list.append('up')
        
        elif move == 'right':
            reversed_catcher_move_list.append('left')
        
        elif move == 'left':
            reversed_catcher_move_list.append('right')
    
    return reversed_catcher_move_list

def catch_runner(catche_sight_x, catcher_sight_y, runner_list, tree_list, t):

    catched_runner = 0
    new_runner_list = []
    
    for runner in runner_list:
        # 술래의 시야에 있으면서 tree에 가려지지 않은 경우

        if runner[0] == catcher_sight_x and runner[1] == catcher_sight_y and [runner[0],runner[1]] not in tree_list:
            catched_runner += 1
        else:
            new_runner_list.append(runner)
    
    total_score = catched_runner * (t+1)

    return new_runner_list, total_score

n, m, h, k = list(map(int, input().split()))

runner_list = []

tree_list =[]

for _ in range(m):
    runner_list.append(list(map(int, input().split())))

for runner in runner_list :
    if runner[2] == 1:
        runner[2] = 'right'
    else:
        runner[2] = 'down'

for _ in range(h):
    tree_list.append(list(map(int, input().split())))


catcher_move_list = make_catcher_move_list(n)[:n*n-1]
reversed_catcher_move_list = make_reversed_catcher_move_list(catcher_move_list)

# 술래의 이동 경로를 list화
all_catcher_trace = catcher_move_list + reversed_catcher_move_list

catcher = [(n-1)//2 + 1, (n-1)//2 + 1]
catcher_idx = 0

total_score = 0
temp = 0
# solution
for t in range(k):
    # print('catcher', catcher)
    # 도망자부터 움직이기
    for r_idx, runner in enumerate(runner_list) :
        
        # 술래와 가까이 있는 경우만 움직이기
        if distance(catcher[0], catcher[1], runner[0], runner[1]):
            
            # 바라보는 방향으로 하나 움직이고
            new_x, new_y = move(runner[0], runner[1], runner[2])
            
            # 움직인 후의 좌표가 격자 내에 있는 경우
            if in_range(new_x, new_y, n):

                # 움직이려는 칸에 술래가 없다면 이동하기, 나무 있든 상관 없음
                #print('catcher',catcher)
                if new_x != catcher[0] or new_y != catcher[1]:
                    runner_list[r_idx][0], runner_list[r_idx][1] = new_x, new_y
            
            # 움직인 후의 좌표가 격자를 벗어나는 경우
            else:
                
                # 먼저 방향을 틀어주기
                # 그 후 이동하기
                if runner[2] == 'up':
                    runner_list[r_idx][2] = 'down'
                    new_x, new_y = move(runner[0], runner[1], 'down')
                    # 움직이려는 칸에 술래가 없다면 이동하기, 나무 있든 상관 없음
                    if new_x != catcher[0] or new_y != catcher[1]:
                        runner_list[r_idx][0], runner_list[r_idx][1] = new_x, new_y

                elif runner[2] == 'down':
                    runner_list[r_idx][2] = 'up'
                    new_x, new_y = move(runner[0], runner[1], 'up')

                    if new_x != catcher[0] or new_y != catcher[1]:
                        runner_list[r_idx][0], runner_list[r_idx][1] = new_x, new_y

                elif runner[2] == 'right':
                    runner_list[r_idx][2] = 'left'
                    new_x, new_y = move(runner[0], runner[1], 'left')

                    if new_x != catcher[0] or new_y != catcher[1]:
                        runner_list[r_idx][0], runner_list[r_idx][1] = new_x, new_y

                elif runner[2] == 'left':
                    runner_list[r_idx][2] = 'right'
                    new_x, new_y = move(runner[0], runner[1], 'right')

                    if new_x != catcher[0] or new_y != catcher[1]:
                        runner_list[r_idx][0], runner_list[r_idx][1] = new_x, new_y

    # 술래 움직이기
    new_catcher_x, new_catcher_y = move(catcher[0], catcher[1], all_catcher_trace[catcher_idx])
    catcher = [new_catcher_x, new_catcher_y]
    catcher_idx += 1
    # print('catcher_idx', catcher_idx)

    if catcher_idx == len(all_catcher_trace):
        catcher_idx = 0
    # 현재의 방향에서 술래잡기 시작
    # 현위치 
    catcher_sight_x, catcher_sight_y = new_catcher_x, new_catcher_y
    runner_list, earned_score = catch_runner(catcher_sight_x, catcher_sight_y, runner_list, tree_list, t)

    total_score += earned_score
    catcher_direction = all_catcher_trace[catcher_idx]

    if catcher_direction == 'up':
        for _ in range(2):
            catcher_sight_x -= 1

            if in_range(catcher_sight_x, catcher_sight_y, n):
                runner_list, earned_score = catch_runner(catcher_sight_x, catcher_sight_y, runner_list, tree_list, t)
                total_score += earned_score
    
    elif catcher_direction == 'down':
        for _ in range(2):
            catcher_sight_x += 1
            
            if in_range(catcher_sight_x, catcher_sight_y, n):
                runner_list, earned_score = catch_runner(catcher_sight_x, catcher_sight_y, runner_list, tree_list, t)
                total_score += earned_score
    
    elif catcher_direction == 'right':
        for _ in range(2):
            catcher_sight_y += 1
            
            if in_range(catcher_sight_x, catcher_sight_y, n):
                runner_list, earned_score = catch_runner(catcher_sight_x, catcher_sight_y, runner_list, tree_list, t)
                total_score += earned_score
    
    elif catcher_direction == 'left':
        for _ in range(2):
            catcher_sight_y -= 1
            
            if in_range(catcher_sight_x, catcher_sight_y, n):
                runner_list, earned_score = catch_runner(catcher_sight_x, catcher_sight_y, runner_list, tree_list, t)
                total_score += earned_score
    if temp != total_score:
        print("현재 %d턴!! %d득점! 누적점수는 %d!!" %(t+1, total_score - temp, total_score))
        temp = total_score
print(total_score)

