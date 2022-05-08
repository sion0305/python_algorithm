import sys 
sys.stdin=open("김태원/input.txt", "rt")

n= int(input())
answer = list(map(int, input().split()))

score = 0
res = 0
for x in answer:
    if x == 1:
        score += 1
        res += score
    else:
        score = 0

print(res)
        