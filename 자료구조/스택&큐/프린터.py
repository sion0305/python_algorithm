def solution(priorities, location):
    queue = [(i,p) for i, p in enumerate(priorities)] # enumerate() = "index : {i}, value: {p}"
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): # 하나라도 큰게 있으면 append
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer