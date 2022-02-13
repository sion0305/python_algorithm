n = int(input())

for i in range(n):
    a = list(map(str, input().split()))
    answer = float(a[0])
    for j in range(1,len(a)):
        if a[j] == "#":
            answer -= 7
        elif a[j] == "%":
            answer += 5
        elif a[j] == "@":
            answer *= 3
    print("%0.2f" % answer)