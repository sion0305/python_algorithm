n = int(input())

sum = 0
for i in range(n):
    a,b = map(int, input().split())
    sum += b % a
print(sum)