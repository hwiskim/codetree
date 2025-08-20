
def inRange(x, y):
    if x in range(0, n) and y in range(0, n):
        return True
    else:
        return False

def three_check(three):
    global max_num
    count = 0
    for i in range(3):
        for j in range(3):
            if three[i][j] == 1:
                count += 1
    if max_num < count:
        max_num = count

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

re_count = (n - 2)
max_num = 0
for i in range(re_count):
    for j in range(re_count):
        a = [row[j:j+3] for row in grid[i:i+3]]
        three_check(a)
print(max_num)