from collections import deque

n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

d_u = deque(u)
d_d = deque(d)
for _ in range(t):
    d_u.appendleft(d_d.pop())
    d_d.appendleft(d_u.pop())
for i in range(len(d_u)):
    if i < len(d_u) - 1:
        print(d_u[i], end=" ")
    else:
        print(d_u[i])
for i in range(len(d_d)):
    if i < len(d_d) - 1:
        print(d_d[i], end=" ")
    else:
        print(d_d[i])