import sys
import numpy
sys.stdin=open("김태원/input.txt", "rt")

n, m = map(int, input().split())

cnt = [0]*(n+m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

tmp = max(cnt)
print(numpy.where(numpy.array(cnt) == tmp)[0])