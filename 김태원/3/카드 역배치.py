import sys
sys.stdin=open("김태원/input.txt","rt")

# a = [i for i in range(1,21)]
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i] #swap

a.pop(0)
print(a)