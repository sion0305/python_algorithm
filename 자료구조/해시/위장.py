from collections import Counter
from functools import reduce
# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
def solution(clothes):
    cnt = Counter([kind for name, kind in clothes]) # name / kind 중 KIND만 for문 돌리기
    answer = reduce(lambda x, y : x*(y+1), cnt.values(), 1) - 1
    return answer