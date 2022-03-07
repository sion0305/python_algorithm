n = int(input())
arr = input().split()

x,y = 1,1
dir = [[0,-1], [0,1], [-1,0], [1,0]]
plan = ['L', 'R', 'U', 'D']

for d in arr:
    for i in range(len(plan)):
        if d == plan[i]:
            nx = x + dir[i][0]
            ny = y + dir[i][1]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx, ny
    
print(x,y)
