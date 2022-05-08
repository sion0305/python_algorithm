import sys
sys.stdin=open("김태원/input.txt", "rt")

str = input()

res = 0
for s in str:
    if s.isdigit():
        res = res*10 + int(s)
print(res)

cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)