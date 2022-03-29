from itertools import *
def solution(sentences, n):
    answer = 0
    selected = []
    scores = []

    for s in sentences:
        s_temp = ''.join(set(s.lower().replace(' ','')))
        score = len(s)
        for c in s:
            if c.isupper():
                score += 1
        if not s.islower():
            s_temp += 'S' # shift가 필요할때
        
        selected.append(s_temp)
        scores.append(score)
    
    # 점수 계산하기
    for k in range(1, len(selected)+1):
        printList = list(combinations(enumerate(selected), k))
        for select in printList:
            temp = ''
            score_temp = 0
            for s in select:
                temp += s[1]
                score_temp += scores[s[0]]
            s_temp = ''.join(set(temp))
            if len(s_temp) > n:
                continue
            answer = max(answer, score_temp)
            print(answer)
    return answer

s = ["line in line", "LINE", "in lion"]
n = 5

s= ["ABcD", "bdbc", "a", "Line neWs"]
n = 7

print(solution(s,n))