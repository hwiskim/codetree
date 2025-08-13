dir_num = {'E':0, 'S':1, 'W':2, 'N': 3}
dx,dy = [1,0,-1,0], [0,-1,0,1]
nx = ny = 0
n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

for i in range(n):
    nx, ny = nx + dx[dir_num[dir[i]]]*dist[i], ny + dy[dir_num[dir[i]]]*dist[i]
print("%d %d" % (nx,ny))