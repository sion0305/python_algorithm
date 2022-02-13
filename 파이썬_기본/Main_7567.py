bowl = list(input())
sum = 0
for i in range(len(bowl)):
    if i == 0 :
        sum += 10
    elif bowl[i-1] == bowl[i]:
        sum += 5
    else:
        sum += 10
print(sum)