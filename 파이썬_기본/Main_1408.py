h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

now = h1 * 3600 + m1 * 60 + s1
start = h2 * 3600 + m2 * 60 + s2

if h1 > h2:
    start += 24 * 3600

time = start - now

a = str(time//3600) 
b = str(time % 3600 // 60) 
c = str(time % 3600 % 60)

if len(a) == 1:
    a = "0" + str(time//3600)
if len(b) == 1:
    b = "0" + str(time % 3600 // 60) 
if len(c) == 1:
    c = "0" + str(time % 3600 % 60)

print(a + ":" + b + ":" + c)