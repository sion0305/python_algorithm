def solution(survey, choices):
    answer = ''

    score = [[3,0], [2,0], [1,0], [0,0], [0,1], [0,2], [0,3]]
    save = list()
    for s, c in zip(survey, choices):
        first = s[0]
        second = s[1]
        save.append([first, ])





    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"] 
choices = [5, 3, 2, 7, 5]

print(solution(survey, choices))