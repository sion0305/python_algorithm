plan = input()

row = int(plan[1])
column = int(ord(plan[0])) - int(ord('a')) + 1

dirs = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[2,-1],[-1,-2]]

result = 0
for x, y in dirs:
    nr = row + x
    nc = column + y
    if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8:
        result += 1
print(result)