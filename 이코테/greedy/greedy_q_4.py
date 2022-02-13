n = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = 1
for a in arr:
    if result < a:
        break
    result += a

print(result)