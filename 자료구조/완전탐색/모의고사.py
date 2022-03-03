def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    result = []
    score = [0,0,0]

    for i in range(len(answers)):
        if pattern1[i%len(pattern1)] == answers[i]:
            score[0] += 1
        if pattern2[i%len(pattern2)] == answers[i]:
            score[1] += 1
        if pattern3[i%len(pattern3)] == answers[i]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result