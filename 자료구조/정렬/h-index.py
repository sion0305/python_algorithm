def solution(citations):
    citations.sort()
    for i, j in enumerate(citations):
        if j >= len(citations) - i:
            return len(citations)- i
    return 0