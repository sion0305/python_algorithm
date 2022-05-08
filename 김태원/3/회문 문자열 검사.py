import sys 
# sys.stdin = open("김태원/input.txt", "rt")

n = int(input())

for i in range(n):
    str = input().upper()
    reverse = "".join(reversed(str))

    if str == reverse:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
