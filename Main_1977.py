m = int(input())
n = int(input())

i = 1
arr = []
while i ** 2 <= n:
    if  m <= i ** 2 <= n:
        arr.append(i ** 2)
    i += 1

if arr == []:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])