n = int(input())

for i in range(n):
    total = int(input())
    for j in range(int(input())):
        a,b = map(int, input().split())
        total += a * b
    print(total)