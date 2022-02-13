arr =[]
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        arr.append(a)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)