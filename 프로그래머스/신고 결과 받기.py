from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)

    id_dict = defaultdict(set)
    num_dict = defaultdict(int)

    suspended = []

    for r in report:
        r_a, r_b = r.split()
        
        id_dict[r_a].add(r_b)
        num_dict[r_b] += 1

        if num_dict[r_b] == k:
            suspended.append(r_b)

    for s in suspended:
        for i in range(len(id_list)):
            if s in id_dict[id_list[i]]:
                answer[i] += 1
    return answer