from collections import deque
def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = (sum1 + sum2) / 2

    if sum1 == sum2:
        return answer

    while True:
        if (sum1 > sum2) :
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp

        if not queue1 or not queue2:
            return -1
        answer += 1

        if sum1 == total:
            break

    return answer


q1 = [3, 2, 7, 2]
q2 = [4, 6, 5, 1]
print(solution(q1, q2))