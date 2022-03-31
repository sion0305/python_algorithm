from itertools import permutations
def solution(A, B):
    answer = -1

    perm = set(permutations(B, len(B)))
    print(perm)
    
    for a,b,c,d in perm:
        score = 0
        if a > A[0]:
            score += 1
        if b > A[1]:
            score += 1
        if c > A[2]:
            score +=1
        if d > A[3]:
            score += 1
        answer = max(answer, score)

    return answer

a = [5, 1, 3, 7]
b = [2, 2, 6, 8]

# a = [2, 2, 2, 2]
# b = [1, 1, 1, 1]
print(solution(a, b))