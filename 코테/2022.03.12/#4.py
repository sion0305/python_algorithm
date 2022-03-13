def solution(n, edges):
    answer = 0
    cost = [[100001 for _ in range(n)] for _ in range(n)]

    #트리 정리
    for i, j in edges:
        cost[i][j] , cost[j][i] = 1, 1
    
    #플로이드-워셜 
    for k in range(n): 
        for i in range(n):
            for j in range(n):
                if i == j: 
                    cost[i][j] = 0 
                else: 
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
        
    for k in range(n): 
        for i in range(n):
            for j in range(n):
                if cost[k][i] == 0 or cost[i][j] == 0 or cost[k][j] == 0:
                    continue
                if cost[k][i] + cost[i][j] == cost[k][j]:
                    print(k,i,j)
                    answer += 1
    
    return answer

n = 5
edges = [[0, 1], [0, 2], [1, 3], [1, 4]] #16
# 4, [[2, 3], [0, 1], [1, 2]]
# 기댓값 〉8
print(solution(n, edges))