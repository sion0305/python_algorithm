from heapq import *

def solution(scoville, k):
    count = 0
    heapify(scoville) # list -> heap
    while scoville[0] < k and len(scoville) > 1:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        count += 1
    return count if scoville[0] >= k else -1