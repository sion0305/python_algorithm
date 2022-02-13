n = int(input())

arr = list(map(int, input().split()))

count = 0
for i in arr:
    flag = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                flag = 1
        if flag == 0:
            count += 1
print(count)
    