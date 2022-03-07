s = input()
result = []
value = 0

for x in s:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)
    
result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))