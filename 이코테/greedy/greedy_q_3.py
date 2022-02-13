data = input()

count = 0
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        count += 1

print((count+1)//2)