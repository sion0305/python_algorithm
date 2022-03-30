def solution(s):
    answer = []
    temp = []
    keypad = [[".","Q","Z"], ["A","B","C"], ["D","E","F"], 
            ["G","H","I"], ["J","K","L"], ["M","N","O"],
            ["P","R","S"], ["T","U","V"], ["W","X","Y"]]

    count = 0
    pre = int(s[0])
    for letter in s:
        button = int(letter)
        if button == 0:
            print('zero', pre-1, count, keypad[pre-1][count])
            answer.append(temp.pop())
            count = 0
            temp.clear()
            continue
        if not temp: # temp가 비어있으면
            print('empty', pre-1, count, keypad[pre-1][count])
            temp.append(keypad[button-1][count])
        elif pre == button:
            count += 1
            print('연속', pre-1, count, keypad[pre-1][count])
            temp.append(keypad[button-1][count])
        else:
            print('달라', pre-1, count, keypad[pre-1][count])
            answer.append(temp.pop())
            temp.clear()
            count = 0
            pre = button
            temp.append(keypad[button-1][count])
    if temp:
        answer.append(temp.pop())

    return ''.join(answer)


s = "44335550555666"
print(solution(s))