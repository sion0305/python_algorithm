s = input()
answer = len(s)

for step in range(1, len(s) // 2 + 1):
    compressed = ""
    temp = s[0:step]
    count = 1
    for i in range(step,len(s),step):
        if temp == s[i:i+step]:
            count += 1
        else:
            compressed += str(count) + temp if count >=2 else temp
            temp = s[i:i+step]
            count = 1
    compressed += str(count) + temp if count >=2 else temp
    answer = min(answer, len(compressed))
print(answer)