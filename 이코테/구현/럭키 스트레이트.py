num = input()

sum = 0
for i in range(len(num) // 2):
    sum += int(num[i])

for i in range(len(num) // 2 , len(num)):
    sum -= int(num[i])

if sum == 0:
    print("LUCKY")
else:
    print("READY")