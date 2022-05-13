import sys
# sys.stdin=open("김태원/input.txt", "rt")

n = int(input())

a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))

a.extend(b)
a.sort()
for i in a:
    print(i, end=' ')