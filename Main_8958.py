n = int(input())

for i in range(n):
    a = input()
    s = list(a)
    sum = 0
    b = 1
    for i in s:
        if i == 'O':
            sum += b
            b += 1
        else:
            b = 1
    print(sum)