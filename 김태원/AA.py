import sys
# sys.stdin=open("김태원/input.txt","rt")

n, k= map(int, input().split())

count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
    if count == k:
        print(i)
        break
else: # for-else 구문이 있음
    print(-1)