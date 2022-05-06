import time
import sys
from itertools import *
sys.stdin=open("김태원/input.txt","rt")

start= time.time()
n, k = map(int, input().split())

numList = list(map(int, input().split()))
a = list(combinations(numList, 3))
res = set()

for i,j,m in a:
    res.add(i+j+m)

res = list(res)
res.sort(reverse=True)
print(res[k-1])

end = time.time()
print(f"{end-start:.10f} sec")