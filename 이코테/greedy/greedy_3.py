n,m = map(int,input().split())

arr = []
for i in range(n):
    nums = list(map(int, input().split()))
    arr.append(min(nums))

print(max(arr))