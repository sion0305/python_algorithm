def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)} # d = {'classic': [], 'pop': []}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    # d = {'classic': [[500, 0], [150, 2], [800, 3]], 'pop': [[600, 1], [2500, 4]]}
    genreSort = sorted(list(d.keys()), key = lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    # list(d.keys()) = ['pop', 'classic']
    # genreSort = ['pop', 'classic']
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        # temp[:min(len(temp),2)] = [4, 1] / [3, 0]
        answer += temp[:min(len(temp),2)]
    return answer