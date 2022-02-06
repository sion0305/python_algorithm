answer = 0
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    answer += a

print(answer//5)