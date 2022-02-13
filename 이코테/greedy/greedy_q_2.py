data = input()

result = int(data[0])

for i in range(1,len(data)):
    if result > 0:
        result *= int(data[i])
    else:
        result += int(data[i])

print(result)