t = int(input())

for i in range(t):
    n = int(input())
    total = 0
    avg = 0.0
    for i in range(n):
        c, g = map(float,input().split())
        total += c
        avg += g * c
    print(int(total), '%.1f'%(avg/total))