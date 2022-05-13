import sys
sys.stdin=open("김태원/input.txt", "rt")

n, m = map(int, input().split())

a = list(map(int, input().split()))

# res = 0
# for i in range(n+1):
#     for j in range(i, n+1):
#         if sum(a[i:j]) == 3:
#             res += 1

# print(res)

lt, rt = 0, 1
res = a[0]
cnt = 0
while True:
    if res < m:
        if rt < n:
            res += a[rt]
            rt += 1
        else: 
            break
    elif res == m:
        cnt += 1
        res -= a[lt]
        lt += 1
    else:
        res -= a[lt]
        lt += 1
print(cnt)
