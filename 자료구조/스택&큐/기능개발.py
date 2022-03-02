def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s),1]) 
            # 1 [[7, 1]]
            # 1 [[7, 2], [9, 1]]
        else:
            Q[-1][1]+=1 
            # 2 [[7, 2]]
    return [q[1] for q in Q]