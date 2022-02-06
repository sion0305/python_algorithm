t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    A,B = a,b

    while B != 0:
        A = A % B
        A,B = B,A
    print(a*b//A)