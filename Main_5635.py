n = int(input())

arr = []
for i in range(n):
    arr.append(input().split())
arr.sort(key = lambda k : (int(k[3]), int(k[2]), int(k[1])))

print(arr[-1][0])
print(arr[0][0])